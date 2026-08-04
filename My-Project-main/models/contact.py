"""
models/contact.py – Contact form submission model
"""
from datetime import datetime
from models import db


class Contact(db.Model):
    """Stores every contact form submission."""

    __tablename__ = "contacts"

    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(120), nullable=False)
    email     = db.Column(db.String(200), nullable=False)
    subject   = db.Column(db.String(250), nullable=False)
    message   = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        """Serialise the model to a plain dict (JSON-safe)."""
        return {
            "id":        self.id,
            "name":      self.name,
            "email":     self.email,
            "subject":   self.subject,
            "message":   self.message,
            "timestamp": self.timestamp.isoformat(),
        }

    def __repr__(self):
        return f"<Contact id={self.id} name={self.name!r} email={self.email!r}>"
