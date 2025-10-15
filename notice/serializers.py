from rest_framework import serializers
from .models import Announcement, Event, Birthday, Verse, Ministry, PraiseReport, Article

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class BirthdaySerializer(serializers.ModelSerializer):
    date = serializers.DateField(source="date_of_birth")  
    class Meta:
        model = Birthday
        fields = ["id", "name", "image", "message", "date"]

class VerseSerializer(serializers.ModelSerializer):
    week_of = serializers.DateField(source="date")  
    class Meta:
        model = Verse
        fields = ["id", "text", "reference", "date", "week_of"]

class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = "__all__"

# Add to your existing serializers
class PraiseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PraiseReport
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
