from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Announcement, Event, Birthday, Verse, Ministry, PraiseReport, Article
from .serializers import (
    AnnouncementSerializer, EventSerializer, BirthdaySerializer, 
    VerseSerializer, MinistrySerializer, PraiseReportSerializer, ArticleSerializer
)

channel_layer = get_channel_layer()

def broadcast(model_name, data, action="update"):
    """Broadcast update to all connected WebSocket clients"""
    async_to_sync(channel_layer.group_send)(
        "noticeboard_updates",  # Fixed group name
        {
            "type": "send_update",  # Must match consumer method name
            "content": {
                "model": model_name,
                "action": action,
                "data": data
            }
        }
    )

# Update all signal handlers to use the correct group
@receiver(post_save, sender=Announcement)
def announce_update(sender, instance, **kwargs):
    broadcast("announcement", AnnouncementSerializer(instance).data, "save")

@receiver(post_save, sender=Event)
def event_update(sender, instance, **kwargs):
    broadcast("event", EventSerializer(instance).data, "save")

@receiver(post_save, sender=Birthday)
def birthday_update(sender, instance, **kwargs):
    broadcast("birthday", BirthdaySerializer(instance).data, "save")

@receiver(post_save, sender=Verse)
def verse_update(sender, instance, **kwargs):
    broadcast("verse", VerseSerializer(instance).data, "save")

@receiver(post_save, sender=PraiseReport)
def praise_report_update(sender, instance, **kwargs):
    if instance.approved:
        broadcast("praise_report", PraiseReportSerializer(instance).data, "save")

@receiver(post_save, sender=Article)
def article_update(sender, instance, **kwargs):
    if instance.published:
        broadcast("article", ArticleSerializer(instance).data, "save")

# Add delete signals for completeness
@receiver(post_delete, sender=Announcement)
def announce_delete(sender, instance, **kwargs):
    broadcast("announcement", {"id": instance.id}, "delete")

@receiver(post_delete, sender=Event)
def event_delete(sender, instance, **kwargs):
    broadcast("event", {"id": instance.id}, "delete")