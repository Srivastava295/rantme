"""import required modules."""
import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from markdown import markdown
from django.utils.html import mark_safe
# Create your models here.


class Board(models.Model):
    """Board class."""

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        """Return name."""
        return self.name

    def get_posts_count(self):
        """Get posts count."""
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        """Get last post."""
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    """Topic class."""

    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return subject."""
        return self.subject

    def get_page_count(self):
        """Page count."""
        count = self.posts.count()
        pages = count/20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        """Has many pages."""
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        """Get page range."""
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count+1)

    def get_last_ten_posts(self):
        """Get last ten posts."""
        return self.posts.order_by('-created_at')[:10]


class Post(models.Model):
    """Post class."""

    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        """Return message."""
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

    def get_message_as_markdown(self):
        """Get message."""
        return mark_safe(markdown(self.message, safe_mode='escape'))
