"""Forms for creating and editing notes."""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Model form for Note."""

    class Meta:
        model = Note
        fields = ["title", "content"]
