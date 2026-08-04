"""
controllers/main.py – Page-route controller (Blueprint)
Renders every HTML template page.
"""
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


# ── Page routes ──────────────────────────────────────────────────────────────

@main_bp.route("/")
def home():
    return render_template("home.html", active="home")


@main_bp.route("/about")
def about():
    return render_template("about.html", active="about")


@main_bp.route("/projects")
def projects():
    project_list = [
        {
            "title":       "Portfolio Website",
            "description": "A full-stack MVC portfolio built with Flask and SQLite, featuring a REST API contact form and dynamic frontend animations.",
            "tech":        ["Python", "Flask", "SQLite", "HTML/CSS", "JavaScript"],
            "github":      "https://github.com/akshayd",
            "live":        "#",
            "icon":        "💼",
        },
        {
            "title":       "E-Commerce Platform",
            "description": "Responsive online store with product catalog, cart management, and secure checkout built using Django and PostgreSQL.",
            "tech":        ["Django", "PostgreSQL", "Bootstrap", "Stripe API"],
            "github":      "https://github.com/akshayd",
            "live":        "#",
            "icon":        "🛒",
        },
        {
            "title":       "Task Management App",
            "description": "Real-time collaborative task board with drag-and-drop, user authentication, and WebSocket notifications.",
            "tech":        ["React", "Node.js", "MongoDB", "Socket.IO"],
            "github":      "https://github.com/akshayd",
            "live":        "#",
            "icon":        "✅",
        },
        {
            "title":       "Weather Dashboard",
            "description": "Interactive weather app consuming OpenWeatherMap API with 7-day forecast, charts, and geolocation support.",
            "tech":        ["JavaScript", "Chart.js", "OpenWeatherMap API", "CSS Grid"],
            "github":      "https://github.com/akshayd",
            "live":        "#",
            "icon":        "🌤️",
        },
        {
            "title":       "ML Sentiment Analyser",
            "description": "NLP model for product review sentiment analysis with a Flask web UI, achieving 92 % accuracy on test data.",
            "tech":        ["Python", "scikit-learn", "NLTK", "Flask", "Pandas"],
            "github":      "https://github.com/akshayd",
            "live":        "#",
            "icon":        "🤖",
        },
        {
            "title":       "Hospital Management System",
            "description": "Desktop application for patient records, appointment scheduling, and billing using Java Swing and MySQL.",
            "tech":        ["Java", "MySQL", "Java Swing", "JDBC"],
            "github":      "https://github.com/akshayd",
            "live":        "#",
            "icon":        "🏥",
        },
    ]
    return render_template("projects.html", active="projects", projects=project_list)


@main_bp.route("/certifications")
def certifications():
    cert_list = [
        {
            "title":    "Full Stack Web Development",
            "issuer":   "Udemy",
            "date":     "2024",
            "badge":    "🎓",
            "color":    "#e67e22",
            "verify":   "#",
        },
        {
            "title":    "Python for Data Science",
            "issuer":   "Coursera – IBM",
            "date":     "2023",
            "badge":    "🐍",
            "color":    "#3498db",
            "verify":   "#",
        },
        {
            "title":    "AWS Cloud Practitioner",
            "issuer":   "Amazon Web Services",
            "date":     "2024",
            "badge":    "☁️",
            "color":    "#f39c12",
            "verify":   "#",
        },
        {
            "title":    "React & Next.js Developer",
            "issuer":   "Zero To Mastery",
            "date":     "2023",
            "badge":    "⚛️",
            "color":    "#61dafb",
            "verify":   "#",
        },
        {
            "title":    "SQL & Database Design",
            "issuer":   "LinkedIn Learning",
            "date":     "2023",
            "badge":    "🗄️",
            "color":    "#2ecc71",
            "verify":   "#",
        },
        {
            "title":    "Machine Learning A-Z",
            "issuer":   "Udemy – SuperDataScience",
            "date":     "2024",
            "badge":    "🤖",
            "color":    "#9b59b6",
            "verify":   "#",
        },
    ]
    return render_template("certifications.html", active="certifications", certifications=cert_list)


@main_bp.route("/skills")
def skills():
    skill_groups = [
        {
            "category": "Frontend",
            "icon":     "🎨",
            "skills": [
                {"name": "HTML5",       "level": 95},
                {"name": "CSS3",        "level": 90},
                {"name": "JavaScript",  "level": 88},
                {"name": "React.js",    "level": 80},
                {"name": "Bootstrap",   "level": 85},
            ],
        },
        {
            "category": "Backend",
            "icon":     "⚙️",
            "skills": [
                {"name": "Python",      "level": 92},
                {"name": "Flask",       "level": 88},
                {"name": "Django",      "level": 78},
                {"name": "Node.js",     "level": 72},
                {"name": "REST APIs",   "level": 88},
            ],
        },
        {
            "category": "Database",
            "icon":     "🗄️",
            "skills": [
                {"name": "SQLite",      "level": 90},
                {"name": "MySQL",       "level": 85},
                {"name": "PostgreSQL",  "level": 78},
                {"name": "MongoDB",     "level": 70},
                {"name": "SQLAlchemy",  "level": 85},
            ],
        },
        {
            "category": "Tools & DevOps",
            "icon":     "🛠️",
            "skills": [
                {"name": "Git & GitHub","level": 90},
                {"name": "Docker",      "level": 65},
                {"name": "AWS",         "level": 60},
                {"name": "Linux",       "level": 78},
                {"name": "VS Code",     "level": 95},
            ],
        },
    ]
    return render_template("skills.html", active="skills", skill_groups=skill_groups)


@main_bp.route("/achievements")
def achievements():
    achievement_list = [
        {
            "title":       "Best Project Award",
            "event":       "College Tech Fest 2024",
            "description": "Won 1st place out of 120 teams for building an AI-powered hospital management system.",
            "icon":        "🏆",
            "year":        "2024",
        },
        {
            "title":       "Hackathon Runner-Up",
            "event":       "HackIndia 2023",
            "description": "Secured 2nd place in a 36-hour national hackathon by developing a smart agriculture IoT dashboard.",
            "icon":        "🥈",
            "year":        "2023",
        },
        {
            "title":       "Open Source Contributor",
            "event":       "Hacktoberfest 2023",
            "description": "Completed 5+ accepted pull requests to open-source Python and JavaScript projects on GitHub.",
            "icon":        "🌐",
            "year":        "2023",
        },
        {
            "title":       "Coding Excellence Award",
            "event":       "Department – 2024",
            "description": "Recognised by the department for consistently top-ranking performance in competitive programming.",
            "icon":        "⭐",
            "year":        "2024",
        },
        {
            "title":       "100-Day Coding Streak",
            "event":       "LeetCode",
            "description": "Completed a 100-day consecutive problem-solving streak, solving 300+ problems across various difficulty levels.",
            "icon":        "🔥",
            "year":        "2024",
        },
        {
            "title":       "Scholarship Recipient",
            "event":       "State Merit Scholarship",
            "description": "Awarded state merit scholarship for academic excellence maintaining GPA above 9.0 throughout the programme.",
            "icon":        "🎓",
            "year":        "2022",
        },
    ]
    return render_template("achievements.html", active="achievements", achievements=achievement_list)


@main_bp.route("/contact")
def contact():
    return render_template("contact.html", active="contact")
