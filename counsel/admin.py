from django.contrib import admin
from .models import Counsellor, Client, Comment, CommentReply


@admin.register(Counsellor)
class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'text', 'twitter', 'website', 'reviews', 'date')
    list_filter = ('reviews', 'name', 'date')
    search_fields = ('name', 'text',)
    ordering = ('date', 'reviews')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('reaL_name', 'nick_name', 'time', 'date', 'story', 'hashtag', 'hashtagg')
    list_filter = ('nick_name', 'date', 'hashtag', 'hashtagg')
    search_fields = ('reaL_name', 'nick_name',)
    ordering = ('date', 'time')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'reply')
    list_filter = ('client', 'date')
    search_fields = ('client',)
    ordering = ('date',)


@admin.register(CommentReply)
class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date', 'reply')
    list_filter = ('date',)
    ordering = ('date',)

