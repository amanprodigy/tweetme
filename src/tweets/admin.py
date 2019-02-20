from django.contrib import admin

from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at', 'updated_at']