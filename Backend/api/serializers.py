from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Genre, HomeCollection, HomeCollectionItem, Movie, Profile, WatchProgress, Watchlist

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    thumbnail = serializers.SerializerMethodField()
    backdrop = serializers.SerializerMethodField()
    runtime_label = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'release_date',
            'thumbnail',
            'backdrop',
            'genres',
            'video_url',
            'content_type',
            'duration_minutes',
            'maturity_rating',
            'is_featured',
            'featured_rank',
            'runtime_label',
            'created_at',
        ]

    def get_thumbnail(self, obj):
        return self._build_media_url(obj.thumbnail, self.context.get('request'))

    def get_backdrop(self, obj):
        return self._build_media_url(obj.backdrop, self.context.get('request'))

    def get_runtime_label(self, obj):
        if not obj.duration_minutes:
            return ''

        hours, minutes = divmod(obj.duration_minutes, 60)
        if hours and minutes:
            return f'{hours}h {minutes}m'
        if hours:
            return f'{hours}h'
        return f'{minutes}m'

    def _build_media_url(self, file_field, request):
        if not file_field:
            return None
        if request is not None:
            return request.build_absolute_uri(file_field.url)
        return file_field.url


class HomeCollectionItemSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = HomeCollectionItem
        fields = ['position', 'movie']


class HomeCollectionSerializer(serializers.ModelSerializer):
    items = HomeCollectionItemSerializer(many=True, read_only=True)

    class Meta:
        model = HomeCollection
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'display_style',
            'display_order',
            'items',
        ]


class WatchProgressSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    progress_percent = serializers.SerializerMethodField()

    class Meta:
        model = WatchProgress
        fields = [
            'id',
            'movie',
            'progress_seconds',
            'duration_seconds',
            'episode_label',
            'progress_percent',
            'updated_at',
        ]

    def get_progress_percent(self, obj):
        if not obj.duration_seconds:
            return 0
        return min(100, round((obj.progress_seconds / obj.duration_seconds) * 100))

class WatchlistSerializer(serializers.ModelSerializer):
    movie_details = MovieSerializer(source='movie', read_only=True)

    class Meta:
        model = Watchlist
        fields = ['id', 'movie', 'movie_details', 'added_date']


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    full_name = serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    avatar = serializers.ImageField(write_only=True, required=False, allow_null=True)
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'date_joined',
            'avatar',
            'avatar_url',
        ]

    def get_full_name(self, obj):
        return obj.user.get_full_name().strip()

    def get_avatar_url(self, obj):
        return self._build_media_url(obj.avatar, self.context.get('request'))

    def _build_media_url(self, file_field, request):
        if not file_field:
            return None
        if request is not None:
            return request.build_absolute_uri(file_field.url)
        return file_field.url


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True, trim_whitespace=False)
    new_password = serializers.CharField(write_only=True, trim_whitespace=False)
    confirm_password = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        user = self.context['user']
        current_password = attrs['current_password']
        new_password = attrs['new_password']
        confirm_password = attrs['confirm_password']

        if not user.check_password(current_password):
            raise serializers.ValidationError(
                {'current_password': ['Current password is incorrect.']}
            )

        if new_password != confirm_password:
            raise serializers.ValidationError(
                {'confirm_password': ['New passwords do not match.']}
            )

        if current_password == new_password:
            raise serializers.ValidationError(
                {'new_password': ['Your new password must be different from the current password.']}
            )

        validate_password(new_password, user=user)
        return attrs

    def save(self, **kwargs):
        user = self.context['user']
        user.set_password(self.validated_data['new_password'])
        user.save(update_fields=['password'])
        return user
