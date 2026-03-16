"""
Simple Reminder GUI Application using PyQt6.
"""

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QDateTimeEdit, QLineEdit, QTextEdit,
                             QSpacerItem, QSizePolicy, QHBoxLayout,
                             QPushButton, QMessageBox)
from PyQt6.QtCore import QDateTime
import sys, requests

class ReminderApp(QWidget):
    """
    This class creates a GUI where the user can enter reminder
    details and send them to a server using an API.
    """

    def __init__(self):
        """Initialize the main window."""
        super().__init__()

        # Set window title
        self.setWindowTitle("Add Reminder")

        # Build the UI
        self.setup_ui()

    def setup_ui(self):
        """
        Create and arrange all GUI widgets in the window.
        """

        layout = QVBoxLayout()

        # Date and Time Picker
        self.datetime_label = QLabel("Event Date and Time:")
        self.datetime_picker = QDateTimeEdit()
        self.datetime_picker.setDateTime(QDateTime.currentDateTime())
        self.datetime_picker.setCalendarPopup(True)
        layout.addWidget(self.datetime_label)
        layout.addWidget(self.datetime_picker)

        # Email Input
        self.email_label = QLabel("Email: ")
        self.email_input = QLineEdit("app11flask@gmail.com")
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Reminder Message
        self.reminder_label = QLabel("Reminder: ")
        self.reminder_input = QTextEdit()
        layout.addWidget(self.reminder_label)
        layout.addWidget(self.reminder_input)

        # Repeat interval
        self.repeat_label = QLabel("Repeat Interval: ")
        self.repeat_input = QLineEdit()
        self.repeat_input.setPlaceholderText("e.g., 1d, 2w, 3m")
        layout.addWidget(self.repeat_label)
        layout.addWidget(self.repeat_input)

        # Buttons layout
        button_layout = QHBoxLayout()
        self.submit_button = QPushButton("Add Reminder")
        self.submit_button.clicked.connect(self.submit_reminder)
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)

        # Spacer for better layout spacing
        layout.addSpacerItem(QSpacerItem(50, 50,
                                         QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Expanding))
        
        # Set main layout
        self.setLayout(layout)

    def submit_reminder(self):
        """
        Collect data from input fields and send it to the server
        using an HTTP POST request.
        """

        # Get datetime from picker
        datetime = self.datetime_picker.dateTime().toString("yyyy-MM-dd HH:mm")

        # Split date and time
        date, time = datetime.split(" ")

        # Create data dictionary
        data = {
                "date": date,
                "time": time,
                "email": self.email_input.text(),
                "message": self.reminder_input.toPlainText(),
                "repeat_interval": self.repeat_input.text()
                }

        # Send POST request to API
        response = requests.post(
            # "http://realworldpython.pythonanywhere.com/add"
            "http://127.0.0.1:5000/add",
            json=data)
        
        # If request successful
        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Reminder added successfully!")

            # Clear input fields
            self.reminder_input.clear()
            self.repeat_input.clear()
        else:
            #  If request Fail
            error_msg = response.json()
            # print(error_msg['error'])
            QMessageBox.information(self,"Fail", f"{error_msg['error']}")


# Start application
app = QApplication(sys.argv)

# Create window
window = ReminderApp()

# Show window
window.show()

# Run event loop
sys.exit(app.exec())