import smtplib
from email.message import EmailMessage
from datetime import datetime
import dateutil.relativedelta as relativedelta

from app.utils.file_handler import load_reminders, save_reminders_to_file
from config import EMAIL, PASSWORD


def save_reminder(data):
    reminders = load_reminders()
    reminders.append(data)
    save_reminders_to_file(reminders)


def send_reminders():
    reminders = load_reminders()
    today = datetime.now().strftime("%Y-%m-%d")

    remaining = []

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(EMAIL, PASSWORD)

    for r in reminders:
        if r['date'] == today:
            msg = create_email(r)
            smtp.send_message(msg)

            if r.get('repeat_interval'):
                r['date'] = calculate_next_date(r['date'], r['repeat_interval'])
                remaining.append(r)
        else:
            remaining.append(r)

    save_reminders_to_file(remaining)


def create_email(r):
    msg = EmailMessage()
    msg['Subject'] = "⏰ Reminder"
    msg['From'] = EMAIL
    msg['To'] = r['email']

    msg.set_content(f"""
Message: {r['message']}
Date: {r['date']}
Time: {r['time']}
""")
    return msg


def calculate_next_date(date_str, repeat_interval):
    date = datetime.strptime(date_str, '%Y-%m-%d')

    unit = repeat_interval[-1]
    value = int(repeat_interval[:-1])

    if unit == 'm':
        next_date = date + relativedelta.relativedelta(months=value)
    elif unit == 'w':
        next_date = date + relativedelta.relativedelta(weeks=value)
    elif unit == 'd':
        next_date = date + relativedelta.relativedelta(days=value)

    return next_date.strftime('%Y-%m-%d')