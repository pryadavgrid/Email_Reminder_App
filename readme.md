# ⏰ Python Reminder System

A simple **Python-based Reminder System** that allows users to create reminders using a **desktop GUI application**, store them through a **Flask API**, and automatically send **email notifications** when the reminder date arrives.

This project demonstrates a **complete workflow** involving:

* Desktop GUI (PyQt6)
* REST API (Flask)
* CSV file storage
* Automated email reminders

---

# 📌 Project Overview

The system consists of three main components:

1. **GUI Application (PyQt6)**
   Used by the user to create reminders.

2. **Flask API Server**
   Receives reminder data and stores it in a CSV file.

3. **Reminder Email Script**
   Reads reminders and sends email notifications on the scheduled date.

---

# 🗂 Project Structure

```
reminder-project/
│
├── gui.py                    # PyQt6 GUI application
├── flask_app.py              # Flask API server
├── send_reminders.py         # Email reminder processor
│
├── reminders.csv             # Reminder storage file
├── .env                      # Email credentials
│
└── README.md                 # Project documentation
```

---

# ⚙️ System Workflow

The reminder system works in the following steps:

```
User (GUI Application)
        │
        ▼
Submit Reminder
        │
        ▼
Flask API Server
        │
        ▼
Save Data → reminders.csv
        │
        ▼
Email Reminder Script
        │
        ▼
Check Today's Date
        │
        ▼
Send Email Notification
```

---

# 🖥 File 1 – GUI Application (reminder_gui.py)

## Purpose

This file creates a **desktop interface** where users can add reminders.

## Technologies Used

* PyQt6
* requests library

## Features

The GUI allows users to:

* Select **date and time**
* Enter **email address**
* Enter **reminder message**
* Set **repeat interval**

Example repeat intervals:

```
1d → every 1 day
2w → every 2 weeks
3m → every 3 months
```

## Workflow

```
User enters reminder details
        │
        ▼
Click "Add Reminder"
        │
        ▼
Data converted to JSON
        │
        ▼
HTTP POST request sent to Flask API
```

---

# 🌐 File 2 – Flask API Server (falsk_app.py)

## Purpose

This file acts as the **backend server** for the application.

It receives reminder data from the GUI and stores it in a **CSV file**.

## Technologies Used

* Flask
* CSV module

## API Endpoint

```
POST /add
```

### Example Request

```json
{
  "date": "2026-03-20",
  "time": "18:00",
  "email": "user@example.com",
  "message": "Doctor appointment",
  "repeat_interval": "1d"
}
```

### Process

1. Receive request from GUI
2. Validate required fields
3. Save reminder to `reminders.csv`
4. Return success response

---

# 📁 reminders.csv

The reminders are stored in a CSV file.

Example:

```
date,time,email,message,repeat_interval
2026-03-20,18:00,user@example.com,Doctor appointment,1d
```

---

# 📧 File 3 – Email Reminder Script (send_reminders.py)

## Purpose

This script reads the reminders and sends **email notifications** when the reminder date matches the current date.

## Technologies Used

* smtplib
* email.message
* dotenv
* datetime
* dateutil.relativedelta

## Main Tasks

1. Load reminders from CSV
2. Check today's date
3. Send email reminder
4. Calculate next date for repeating reminders
5. Update CSV file

---

## Email Workflow

```
Read reminders.csv
        │
        ▼
Check today's date
        │
        ▼
If reminder date == today
        │
        ▼
Send Email
        │
        ▼
Calculate next reminder date (if repeat)
        │
        ▼
Update CSV file
```

---

# 🔐 Environment Variables

Create a `.env` file for email credentials.

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

---

# ▶️ How to Run the Project

## 1️⃣ Install Dependencies

```
pip install pyqt6 flask python-dotenv python-dateutil requests
```

---

## 2️⃣ Start Flask Server

```
python falsk_app.py
```

Server runs on:

```
http://127.0.0.1:5000
```

---

## 3️⃣ Run GUI Application

```
python reminder_gui.py
```

---

## 4️⃣ Run Email Reminder Script

```
python send_reminders.py
```

You can schedule this script using:

* **Cron Job (Linux / Mac)**
* **Task Scheduler (Windows)**

to run daily.

---

# 📊 Example Data Flow

Example reminder:

```
Date: 2026-03-20
Time: 18:00
Email: user@example.com
Message: Doctor appointment
Repeat Interval: 1d
```

Process:

```
User adds reminder in GUI
        │
        ▼
Reminder saved in CSV
        │
        ▼
Email script runs
        │
        ▼
Email sent on scheduled date
        │
        ▼
Next reminder date calculated
```
---

# PyQt6 
```
PyQt6
 │
 ├── QApplication (This is the main controller of the GUI application.)  → runs the app
 ├── QWidget        → window
 ├── QLabel         → text
 ├── QLineEdit      → single text input
 ├── QTextEdit      → multi text input
 ├── QPushButton    → button
 ├── QMessageBox    → popup message
 │
 ├── Layouts
 │     ├── QVBoxLayout → vertical layout
 │     └── QHBoxLayout → horizontal layout
 │
 ├── Date & Time
 │     ├── QDateTime
 │     └── QDateTimeEdit
 │
 └── Spacing
       ├── QSpacerItem
       └── QSizePolicy

```