from django.db import models

from django.utils import timezone

class Post(models.Model):
    """A table to store post of users"""
    class Status(models.TextChoices):
        """Add choices to post model"""
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)

    class Meta:
        """Defines metadata of models"""
        ordering = [-'publish']
        indexs = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        """state title of object"""
        return self.title