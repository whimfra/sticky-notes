"""Database models for the Sticky Notes app."""

from django.db import models


class Note(models.Model):
    """A single sticky note with a title and content."""

    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        """Return a human-friendly label for the note."""
        return self.title
