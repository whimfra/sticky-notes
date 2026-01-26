"""Unit tests for the Sticky Notes app.

Covers:
- Model basics
- CRUD views (list, detail, create, update, delete)
"""

from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTests(TestCase):
    """Tests for the Note model."""

    def test_str_returns_title(self):
        note = Note.objects.create(title="Hello", content="World")
        self.assertEqual(str(note), "Hello")


class NoteViewTests(TestCase):
    """Tests for note CRUD views."""

    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="Test content")

    def test_note_list_page_loads(self):
        response = self.client.get(reverse("notes:note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_page_loads(self):
        response = self.client.get(reverse("notes:note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_create_valid(self):
        data = {"title": "New", "content": "Content"}
        response = self.client.post(reverse("notes:note_create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="New").exists())

    def test_note_create_invalid(self):
        data = {"title": "", "content": "Content"}
        response = self.client.post(reverse("notes:note_create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Note.objects.filter(content="Content", title="").exists())

    def test_note_update(self):
        data = {"title": "Updated", "content": "Updated content"}
        response = self.client.post(
            reverse("notes:note_update", args=[self.note.pk]),
            data,
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated")

    def test_note_delete(self):
        response = self.client.post(reverse("notes:note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
