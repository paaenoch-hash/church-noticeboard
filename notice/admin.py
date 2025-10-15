from django.contrib import admin
from .models import Announcement, Event, Birthday, Verse, Ministry, PraiseReport, Article

# -----------------------------
# Announcement admin
# -----------------------------
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'expires_at', 'pinned', 'is_active']
    search_fields = ['title', 'content', 'author', 'tags']
    list_filter = ['created_at', 'expires_at', 'pinned', 'ministry']


# -----------------------------
# Event admin
# -----------------------------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'location', 'ministry']
    search_fields = ['title', 'description', 'location']
    list_filter = ['event_date', 'ministry']


# -----------------------------
# Birthday admin
# -----------------------------
@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'message']
    search_fields = ['name']
    list_filter = ['date_of_birth']


# -----------------------------
# Verse admin
# -----------------------------
@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ['reference', 'date']
    search_fields = ['reference', 'text']
    list_filter = ['date']


# -----------------------------
# Ministry admin
# -----------------------------
@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'meets']
    search_fields = ['name', 'contact', 'meets', 'description']

@admin.register(PraiseReport)
class PraiseReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date', 'approved']
    list_filter = ['approved', 'date']
    search_fields = ['title', 'testimony', 'author']
    list_editable = ['approved']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published', 'created_at']
    list_filter = ['published', 'category', 'created_at']
    search_fields = ['title', 'content', 'author']
    list_editable = ['published']