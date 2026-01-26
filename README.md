# Sticky Notes Application (Part 2)

This is a simple Django CRUD application for creating, viewing, editing, and deleting sticky notes.

## Project Structure (Overview)

sticky_notes/            Django project configuration (settings, URLs, WSGI/ASGI)
notes/                   Notes application (models, views, forms, templates, tests)
planning/                Planning documents and sequence diagrams
db.sqlite3               SQLite database file (included)

## Setup Instructions

1. Create a virtual environment (recommended):

   Windows (CMD):

   python -m venv .venv

2. Activate the virtual environment:

   .venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt

4. Run migrations (this creates the database tables):

   python manage.py makemigrations
   python manage.py migrate

5. Run the development server:

   python manage.py runserver

6. Open the application in your browser:

   http://127.0.0.1:8000/

## Running Tests

From the project root directory:

python manage.py test

## Notes About Migrations

If you encounter an error such as:

"no such table: notes_note"

it means migrations have not been applied. Run:

python manage.py migrate

The SQLite database file (db.sqlite3) is included so the application can run immediately once migrations are applied.

## Additional Notes

- Templates for the notes application are located inside the notes app.
- The base template is located in sticky_notes/templates.
- Planning documents and diagrams are located in the planning folder.
- This project demonstrates Django project structure, CRUD functionality, migrations, and basic testing.
