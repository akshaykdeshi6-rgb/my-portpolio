# Akshay D — Full-Stack Portfolio Web Application

A professional, modern, and high-performance full-stack developer portfolio built using the **Model-View-Controller (MVC)** architectural pattern. 

The frontend uses curated color palettes, elegant typography (Cormorant Garamond + Inter), scroll-reveal transitions, responsive structures, and matching styling conforming to modern aesthetic design guidelines. The backend uses Python & Flask with SQLite for persistence and REST API calls for asynchronous contact submission.

---

## 🛠️ Technology Stack
.
- **Frontend**: HTML5, Vanilla CSS3 (Custom design system), Vanilla JS (ES6)
- **Backend Framework**: Python (Flask)
- **Database**: SQLite (via Flask-SQLAlchemy ORM)
- **Dependency Management**: `uv` (Fast Python packaging tool)

---

## 📂 Project Structure (MVC Model)

```text
Akshay D portpolio/
├── app.py                    # Application entry point (Initialises DB, configuration & blueprints)
├── config.py                 # Application configurations (SQLite DB paths, dev/prod modes)
├── models/
│   ├── __init__.py           # Shared SQLAlchemy database instance
│   └── contact.py            # [MODEL] Contact DB structure (Name, Email, Message, etc.)
├── controllers/
│   ├── __init__.py
│   ├── main.py               # [CONTROLLER] Handles page routing for the 7 views
│   └── api.py                # [CONTROLLER] REST API endpoints for contact form POST & GET messages
├── frontend/                 # Separated frontend codes
│   ├── static/               # Assets served directly by Flask
│   │   ├── css/              # Module-specific styling
│   │   │   ├── main.css      # Design tokens, resets, navigation & layout
│   │   │   ├── home.css      # Custom styling matching reference layout
│   │   │   ├── about.css
│   │   │   ├── projects.css
│   │   │   ├── certifications.css
│   │   │   ├── skills.css
│   │   │   ├── achievements.css
│   │   │   └── contact.css
│   │   ├── js/
│   │   │   ├── main.js       # Navigation scroll triggers, scroll reveal animations
│   │   │   └── contact.js    # Asynchronous AJAX submission to REST API
│   │   └── images/
│   │       └── profile.jpg   # Profile photo headshot asset
│   └── templates/            # HTML pages structure (Jinja2 templates)
│       ├── base.html         # Base layout skeleton (Header, footer, CDN fonts)
│       ├── home.html         # Hero columns landing page
│       ├── about.html        # Experience timeline & bio details
│       ├── projects.html     # Dynamic list of projects
│       ├── certifications.html # Professional credentials & verification links
│       ├── skills.html       # Skill categories with scroll-animated progress indicators
│       ├── achievements.html # Award milestones & certifications
│       └── contact.html      # Interactive contact form
├── instance/
│   └── portfolio.db          # Auto-created SQLite database (ignored in git)
├── pyproject.toml            # uv project dependency schema
├── .python-version           # Target python version anchor
├── .gitignore                # Pushes clean, artifact-free code to GitHub
└── README.md                 # Project guide (this file)
```

---

## ⚡ Setup & Installation

This project is configured to use the extremely fast Python package manager **`uv`**. Follow these simple commands to set up the workspace:

### 1. Prerequisite
Ensure you have `uv` installed. If you don't have it, install it using:
```powershell
# On Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. Create Virtual Environment & Install Dependencies
Run the following command inside the project root directory. `uv` will automatically read `pyproject.toml` and configure your environment:
```bash
# Sync package locks, create a virtual environment (.venv) and install dependencies
uv sync
```

### 3. Start the Flask Application
Run the Flask server:
```bash
# Activates the local virtual environment and runs the web app
uv run python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your web browser to view the application!

---

## 📊 REST API Specifications

### Submit Contact Message
- **Endpoint**: `POST /api/contact`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "name": "Alex Mercer",
    "email": "alex@example.com",
    "subject": "Project Proposal",
    "message": "Hello, I am interested in hiring you for a full-stack project."
  }
  ```
- **Responses**:
  - `201 Created`: Message successfully recorded in SQLite database.
  - `400 Bad Request`: Input validation failed (e.g. empty fields or invalid email).

### Fetch Submitted Contacts (Admin)
- **Endpoint**: `GET /api/contacts`
- **Response**: List of all messages sorted by the most recent submission.
