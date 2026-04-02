Here is your **UPDATED README.md** according to your new structure + manual running (no scheduler) 👍

---

# ⏰ Python Reminder System

A simple **Python-based Reminder System** that allows users to create reminders using a **desktop GUI application**, store them through a **Flask API**, and send **email notifications manually** when needed.

This project demonstrates:

* Desktop GUI (PyQt6)
* REST API (Flask)
* CSV file storage
* Manual email reminder execution

---

# 📌 Project Overview

The system consists of three main components:

1. **GUI Application (PyQt6)**
   Used by the user to create reminders.

2. **Flask API Server**
   Receives reminder data and stores it.

3. **Reminder Service (Manual Run)**
   Sends email reminders when you run it manually.

---

# 🗂 Project Structure

```
reminder-project/
│
├── app/
│   ├── controllers/
│   │   └── reminder_controller.py   # API routes
│   │
│   ├── services/
│   │   ├── reminder_service.py      # Email logic
│   │   └── gui_service.py           # PyQt6 GUI
│   │
│   ├── utils/
│   │   └── file_handler.py          # CSV handling
│   │
│   └── main.py                      # Flask app init
│
├── config.py                        # Environment config
├── run.py                           # Start Flask server
├── .env                             # Email credentials
├── requirements.txt
└── README.md
```

---

# ⚙️ System Workflow

```
User (GUI)
   │
   ▼
Submit Reminder
   │
   ▼
Flask API (Controller)
   │
   ▼
Service Layer
   │
   ▼
CSV File (Storage)
   │
   ▼
Manual Script Run
   │
   ▼
Send Email
```

---

# 🖥 GUI Application (`gui_service.py`)

## Purpose

Provides a **desktop interface** for users.

## Features

* Select date & time
* Enter email
* Enter message
* Set repeat interval

Example:

```
1d → daily
2w → weekly
3m → monthly
```

## Flow

```
User input → JSON → POST request → Flask API
```

---

# 🌐 Flask API (`reminder_controller.py`)

## Endpoint

```
POST /add
```

## Example Request

```json
{
  "date": "2026-03-20",
  "time": "18:00",
  "email": "user@example.com",
  "message": "Doctor appointment",
  "repeat_interval": "1d"
}
```

## Process

1. Validate data
2. Call service layer
3. Save to CSV

---

# ⚙️ Service Layer (`reminder_service.py`)

## Responsibilities

* Save reminders
* Send emails
* Handle repeat logic

## Important

👉 Email sending is **NOT automatic**
👉 You must run it manually

---

# 📁 CSV Storage

Handled by:

```
app/utils/file_handler.py
```

Example:

```
date,time,email,message,repeat_interval
2026-03-20,18:00,user@example.com,Doctor appointment,1d
```

---

# 📧 Email Reminder (Manual Execution)

## How it works

```
Load reminders
   │
   ▼
Check today's date
   │
   ▼
Send email if matched
   │
   ▼
Update next date (if repeat)
```

---

# 🔐 Environment Variables

Create `.env` file:

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

---

# ▶️ How to Run the Project

## 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 2️⃣ Run Flask Server

```
python run.py
```

Runs at:

```
http://127.0.0.1:5000
```

---

## 3️⃣ Run GUI Application

```
python app/services/gui_service.py
```

---

## 4️⃣ Run Email Sender (Manual)

```
python -c "from app.services.reminder_service import send_reminders; send_reminders()"
```

👉 This will send emails for today's reminders

---

# 📊 Example Data Flow

```
User adds reminder
   │
   ▼
Saved in CSV
   │
   ▼
You run email script manually
   │
   ▼
Email sent
   │
   ▼
Next date updated
```

---

# 🧠 PyQt6 Quick Reference

```
PyQt6
 │
 ├── QApplication → run app
 ├── QWidget → window
 ├── QLabel → text
 ├── QLineEdit → input
 ├── QTextEdit → multi input
 ├── QPushButton → button
 ├── QMessageBox → popup
 │
 ├── Layouts
 │   ├── QVBoxLayout
 │   └── QHBoxLayout
 │
 ├── Date & Time
 │   ├── QDateTime
 │   └── QDateTimeEdit
 │
 └── Spacing
     ├── QSpacerItem
     └── QSizePolicy
```

---
