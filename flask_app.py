"""
Flask Reminder API
"""
from flask import Flask, request, jsonify
import csv
import os

# Create Flask application
app = Flask(__name__)

# CSV file name
CSV_FILE = "reminders.csv"

# Ensure CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        # CSV writer with column names
        writer = csv.DictWriter(file, fieldnames=[
            "date", "time", "email", "message", "repeat_interval", "remind_days_before"
        ])
        # Write header row
        writer.writeheader()

@app.route("/add", methods=["POST"])
def add_reminder():
    """
    Receives reminder data as JSON from the client
    and saves it to a CSV file.
    """

    # Get JSON data from request
    data = request.json

    # Required fields for reminder
    required_fields = ["date", "time", "email", "message"]

    # Validate required fields
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        # Open CSV file in append mode
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "date", "time", "email", "message", "repeat_interval"])
            
            # Write reminder data to CSV
            writer.writerow({
                "date": data.get("date"),
                "time": data.get("time"),
                "email": data.get("email"),
                "message": data.get("message"),
                "repeat_interval": data.get("repeat_interval", "")
            })

        # Success response
        return jsonify({"status": "ok"}), 200

    except Exception as e:
        # Error response
        return jsonify({"error": str(e)}), 500

# Run the Flask server
if __name__ == "__main__":
    app.run()