from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class ContentType(models.TextChoices):
        MOVIE = 'movie', 'Movie'
        SERIES = 'series', 'Series'

    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    backdrop = models.ImageField(upload_to='backdrops/', null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    video_url = models.URLField(max_length=500)
    content_type = models.CharField(
        max_length=20,
        choices=ContentType.choices,
        default=ContentType.MOVIE,
    )
    duration_minutes = models.PositiveIntegerField(default=90)
    maturity_rating = models.CharField(max_length=20, blank=True, default='')
    is_featured = models.BooleanField(default=False)
    featured_rank = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HomeCollection(models.Model):
    class DisplayStyle(models.TextChoices):
        POSTER = 'poster', 'Poster'
        LANDSCAPE = 'landscape', 'Landscape'

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255, blank=True)
    display_style = models.CharField(
        max_length=20,
        choices=DisplayStyle.choices,
        default=DisplayStyle.POSTER,
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    movies = models.ManyToManyField(
        Movie,
        through='HomeCollectionItem',
        related_name='home_collections',
    )

    class Meta:
        ordering = ['display_order', 'title']

    def __str__(self):
        return self.title


class HomeCollectionItem(models.Model):
    collection = models.ForeignKey(
        HomeCollection,
        on_delete=models.CASCADE,
        related_name='items',
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='collection_items',
    )
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position', 'id']
        constraints = [
            models.UniqueConstraint(
                fields=['collection', 'movie'],
                name='unique_home_collection_movie',
            )
        ]

    def __str__(self):
        return f'{self.collection.title} - {self.movie.title}'

    def save(self, *args, **kwargs):
        if self.collection_id and self.position <= 0:
            max_position = (
                HomeCollectionItem.objects.filter(collection_id=self.collection_id)
                .exclude(pk=self.pk)
                .aggregate(max_position=Max('position'))
                .get('max_position')
                or 0
            )
            self.position = max_position + 1

        super().save(*args, **kwargs)


class WatchProgress(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='watch_progress',
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='watch_progress',
    )
    progress_seconds = models.PositiveIntegerField(default=0)
    duration_seconds = models.PositiveIntegerField(default=0)
    episode_label = models.CharField(max_length=120, blank=True, default='')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie'],
                name='unique_watch_progress',
            )
        ]

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
        constraints = [
            models.UniqueConstraint(fields=['user', 'movie'], name='unique_user_movie')
        ]

    def __str__(self):
        return f"{self.user.username}'s Watchlist"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
