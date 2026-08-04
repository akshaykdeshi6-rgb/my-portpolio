"""
controllers/api.py – REST API controllers for contact form submissions.
"""
from flask import Blueprint, jsonify, request
from models import db
from models.contact import Contact

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/contact", methods=["POST"])
def submit_contact():
    """
    POST /api/contact
    Expects JSON payload with name, email, subject, and message.
    Stores the submission in the SQLite database and returns the created object.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No input data provided"}), 400

        name    = data.get("name", "").strip()
        email   = data.get("email", "").strip()
        subject = data.get("subject", "").strip()
        message = data.get("message", "").strip()

        # Validate input
        errors = {}
        if not name:
            errors["name"] = "Name is required"
        if not email:
            errors["email"] = "Email is required"
        elif "@" not in email:
            errors["email"] = "Invalid email format"
        if not subject:
            errors["subject"] = "Subject is required"
        if not message:
            errors["message"] = "Message is required"

        if errors:
            return jsonify({"status": "error", "message": "Validation failed", "errors": errors}), 400

        # Create contact entry
        new_contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        db.session.add(new_contact)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Message stored successfully!",
            "data": new_contact.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": f"Server error: {str(e)}"}), 500


@api_bp.route("/contacts", methods=["GET"])
def get_contacts():
    """
    GET /api/contacts
    Retrieves all stored contact messages.
    """
    try:
        contacts = Contact.query.order_by(Contact.timestamp.desc()).all()
        return jsonify({
            "status": "success",
            "count": len(contacts),
            "data": [c.to_dict() for c in contacts]
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": f"Server error: {str(e)}"}), 500
