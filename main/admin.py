from django.contrib import admin
from .models import *


@admin.register(Movie)
class AdminMovieDisplay(admin.ModelAdmin):
    fields = ('title', 'description', 'author', 'video', 'genre', 'image', 'rel_date')
    search_fields = ('title', )


@admin.register(Genre)
class AdminGenreDisplay(admin.ModelAdmin):
    readonly_fields = ('slug', )
    search_fields = ('title', )


@admin.register(Comment)
class AdminCommentDisplay(admin.ModelAdmin):
    list_display = ('description', 'movie', 'user')
    list_filter = ('date', )
    search_fields = ('description', 'movie', 'user')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)