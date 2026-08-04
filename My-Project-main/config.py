"""
config.py – Application configuration for Akshay D Portfolio
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    """Base configuration shared across environments."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

    # ── SQLite database stored in instance/ folder ──
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR / 'instance' / 'portfolio.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ── Template & static folders ──
    TEMPLATE_FOLDER = BASE_DIR / "frontend" / "templates"
    STATIC_FOLDER   = BASE_DIR / "frontend" / "static"
    STATIC_URL_PATH = "/static"


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


# Active configuration (default: development)
config_map = {
    "development": DevelopmentConfig,
    "production":  ProductionConfig,
}

ActiveConfig = config_map.get(os.environ.get("FLASK_ENV", "development"), DevelopmentConfig)
