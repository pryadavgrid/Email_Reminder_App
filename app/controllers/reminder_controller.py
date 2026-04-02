from flask import request, jsonify
from app.main import app
from app.services.reminder_service import save_reminder

@app.route("/add", methods=["POST"])
def add_reminder():
    data = request.json

    required_fields = ["date", "time", "email", "message"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        save_reminder(data)
        return jsonify({"status": "ok"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500