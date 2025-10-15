from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, decorators, response, status,  parsers
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Announcement, Event, Verse, Birthday, Ministry
from .models import PraiseReport, Article
from .serializers import (
    AnnouncementSerializer, EventSerializer, VerseSerializer,
    BirthdaySerializer, MinistrySerializer ,PraiseReportSerializer, ArticleSerializer
)
from django.utils import timezone
from rest_framework import decorators, response
from rest_framework import permissions


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "body", "ministry", "tags"]
    ordering_fields = ["posted_at", "expires_at", "pinned"]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @decorators.action(detail=False, methods=["get"], url_path="active")
    def active(self, request):
        """Return only active (non-expired) announcements"""
        now = timezone.now()
        qs = self.get_queryset().filter(expires_at__gte=now)
        serializer = self.get_serializer(qs, many=True)
        return response.Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "location", "ministry", "description"]
    ordering_fields = ["start", "end"]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]

    @decorators.action(detail=False, methods=["get"], url_path="upcoming")
    def upcoming(self, request):
        """Return events happening today or in the future"""
        today = timezone.now().date()
        qs = self.get_queryset().filter(event_date__gte=today)
        serializer = self.get_serializer(qs, many=True)
        return response.Response(serializer.data)

class VerseViewSet(viewsets.ModelViewSet):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["ref", "text"]
    ordering_fields = ["date"]

    
    
    @decorators.action(detail=False, methods=["get", "put"], url_path="week")
    def week(self, request):
        if request.method.lower() == "get":
            v = Verse.objects.order_by("-date").first()
            if not v:
                return response.Response({"detail": "No verse set"}, status=status.HTTP_404_NOT_FOUND)
            return response.Response(self.get_serializer(v).data)
        # PUT: create a new verse record
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        Verse.objects.create(**ser.validated_data)
        return response.Response(ser.data, status=status.HTTP_201_CREATED)

class BirthdayViewSet(viewsets.ModelViewSet):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["date"]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]

    @decorators.action(detail=False, methods=["get"], url_path="this-week")
    def this_week(self, request):
        """Return birthdays within the next 7 days"""
        today = timezone.now().date()
        end_of_week = today + timedelta(days=7)
        qs = self.get_queryset().filter(date_of_birth__range=(today, end_of_week))
        serializer = self.get_serializer(qs, many=True)
        return response.Response(serializer.data)

class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "contact", "meets", "description"]
    ordering_fields = ["name"]


class PraiseReportViewSet(viewsets.ModelViewSet):
    queryset = PraiseReport.objects.filter(approved=True)  # Only show approved
    serializer_class = PraiseReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "testimony", "author"]
    ordering_fields = ["date", "created_at"]

    @decorators.action(detail=False, methods=["get"], url_path="recent")
    def recent(self, request):
        """Return recent praise reports (last 30 days)"""
        last_month = timezone.now() - timedelta(days=30)
        qs = self.get_queryset().filter(created_at__gte=last_month)
        serializer = self.get_serializer(qs, many=True)
        return response.Response(serializer.data)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(published=True)  
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content", "author", "category"]
    ordering_fields = ["created_at", "updated_at"]

    @decorators.action(detail=False, methods=["get"], url_path="categories")
    def categories(self, request):
        """Return list of available categories"""
        categories = Article.objects.filter(published=True).values_list('category', flat=True).distinct()
        return response.Response([cat for cat in categories if cat])