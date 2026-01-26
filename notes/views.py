"""Views for the Sticky Notes app (CRUD)."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display a list of all notes (newest first)."""
    notes = Note.objects.order_by("-id")
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    """Display a single note by primary key."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Create a new note."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:note_list")
    else:
        form = NoteForm()

    return render(
        request,
        "notes/note_form.html",
        {"form": form, "page_title": "Create Note", "button_text": "Save"},
    )


def note_update(request, pk):
    """Edit an existing note."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:note_list")
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "notes/note_form.html",
        {"form": form, "page_title": "Edit Note", "button_text": "Update"},
    )


def note_delete(request, pk):
    """Delete a note after confirmation."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("notes:note_list")

    return render(request, "notes/note_confirm_delete.html", {"note": note})
