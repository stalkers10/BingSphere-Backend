from django.contrib import admin
from .models import Genre, HomeCollection, HomeCollectionItem, Movie, Profile, WatchProgress, Watchlist

admin.site.register(Genre)
admin.site.register(Watchlist)
admin.site.register(WatchProgress)
admin.site.register(Profile)


class HomeCollectionItemInline(admin.TabularInline):
    model = HomeCollectionItem
    extra = 1


@admin.register(HomeCollection)
class HomeCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display_style', 'display_order', 'is_active')
    list_filter = ('display_style', 'is_active')
    search_fields = ('title', 'slug', 'description')
    ordering = ('display_order', 'title')
    inlines = [HomeCollectionItemInline]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'release_date', 'is_featured', 'created_at')
    list_filter = ('content_type', 'genres', 'release_date', 'is_featured')
    search_fields = ('title', 'description')
    ordering = ('featured_rank', '-created_at')
