import csv
import os

FILE_PATH = "app/utils/reminders.csv"


def ensure_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "date", "time", "email", "message", "repeat_interval"
            ])
            writer.writeheader()


def load_reminders():
    ensure_file()

    with open(FILE_PATH) as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_reminders_to_file(reminders):
    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "date", "time", "email", "message", "repeat_interval"
        ])
        writer.writeheader()
        writer.writerows(reminders)