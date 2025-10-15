from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnnouncementViewSet, EventViewSet, VerseViewSet,
    BirthdayViewSet, MinistryViewSet, PraiseReportViewSet,ArticleViewSet
)

router = DefaultRouter()
router.register(r"announcements", AnnouncementViewSet, basename="announcement")
router.register(r"events", EventViewSet, basename="event")
router.register(r"verses", VerseViewSet, basename="verse")
router.register(r"birthdays", BirthdayViewSet, basename="birthday")
router.register(r"ministries", MinistryViewSet, basename="ministry")
router.register(r"praise-reports", PraiseReportViewSet, basename="praisereport")
router.register(r"articles", ArticleViewSet, basename="article")

urlpatterns = [
    path("", include(router.urls)),
]
