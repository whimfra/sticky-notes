"""Admin configuration for the Sticky Notes app."""

from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin display settings for notes."""

    list_display = ("id", "title")
    search_fields = ("title", "content")
