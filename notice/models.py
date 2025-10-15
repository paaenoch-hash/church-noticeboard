from django.db import models
from django.utils import timezone


def upload_announcement(instance, filename):
    return f"announcements/{instance.title}_{filename}"

def upload_event(instance, filename):
    return f"events/{instance.title}_{filename}"

def upload_birthday(instance, filename):
    return f"birthdays/{instance.name}_{filename}"



class Ministry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=200, blank=True)
    meets = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    ministry = models.ForeignKey(Ministry, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    image = models.ImageField(upload_to=upload_announcement, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        """Return True if the announcement has not expired."""
        return not self.expires_at or self.expires_at >= timezone.now()



class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ministry = models.ForeignKey(Ministry, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=upload_event, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.event_date}"



class Birthday(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    message = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=upload_birthday, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.date_of_birth.strftime('%b %d')})"



class Verse(models.Model):
    reference = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.reference} ({self.date})"

# Add to your existing models
class PraiseReport(models.Model):
    title = models.CharField(max_length=255)
    testimony = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    date = models.DateField(default=timezone.now)
    approved = models.BooleanField(default=False)  # Moderation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)  # e.g., "Teaching", "Devotional"
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title