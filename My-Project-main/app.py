"""
app.py – Portfolio Flask application entry point.
Initialises configuration, SQL database, blueprints, and creates db tables.
"""
import os
from pathlib import Path
from flask import Flask
from config import ActiveConfig
from models import db
from controllers.main import main_bp
from controllers.api import api_bp


def create_app(config_class=ActiveConfig):
    """Factory function to build and configure the Flask application."""
    # Resolve absolute paths for templates and static folders relative to this script
    base_dir = Path(__file__).resolve().parent
    template_folder = str(base_dir / "frontend" / "templates")
    static_folder   = str(base_dir / "frontend" / "static")

    app = Flask(
        __name__,
        template_folder=template_folder,
        static_folder=static_folder,
        static_url_path="/static"
    )

    # Load configuration
    app.config.from_object(config_class)

    # Ensure the instance folder exists (for SQLite database file)
    instance_path = base_dir / "instance"
    instance_path.mkdir(exist_ok=True)

    # Initialise the database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    # Create tables automatically inside app context
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    # Get port from environment or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
