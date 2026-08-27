# 🛡️ Integrated Cyber Crime Management System – Python

## 📌 Project Overview

This project is a desktop-based **Integrated Cyber Crime Management System** developed using Python. It provides a graphical interface for managing cyber-crime complaints, viewing complaint information, monitoring complaint status, and interacting with a simple help chatbot.

The application connects a Python desktop interface to a MySQL database and uses a modern dark-themed interface for navigation and data management.

## 🛠️ Tools & Technologies

- Python
- CustomTkinter
- Tkinter / ttk
- MySQL
- mysql-connector-python
- Pillow (PIL)
- Pandas

## 🎯 Project Objectives

- Provide a centralized interface for cyber-crime complaint management
- Register and store complaints in a MySQL database
- Search and view complaints using Complaint ID
- Display complaint statistics on the dashboard
- Track complaint statuses such as Pending, Investigation, and Resolved
- Provide a simple chatbot for common user questions
- Provide application settings and administration screens

## ✨ Key Features

### 🔐 Login & Splash Screen

The application includes a splash/loading screen followed by a login interface.

### 📊 Dashboard

The dashboard provides complaint statistics and a recent-complaints view. Complaint counts are retrieved from the MySQL database.

### 📝 Register Complaint

Users can enter complaint details including name, email, phone, crime type, and description. Submitted complaints are stored in the MySQL database with a pending status.

### 🔎 View & Search Complaint

Users can search for a complaint using its Complaint ID and view details such as complaint type, status, contact information, and description.

### 🤖 Help Chatbot

The project includes a rule-based chatbot that responds to common questions about registering complaints, checking status, crime types, dashboard features, security, and application settings.

### ⚙️ Settings

The application contains settings for dashboard preferences, application preferences, data management, and related administrative options.

## 🗄️ Database Integration

The application uses **MySQL** for storing and retrieving complaint information. Python communicates with the database through `mysql.connector`.

## 📚 Python Concepts Demonstrated

- Functions
- Conditional statements
- Event-driven programming
- GUI development
- Database connectivity
- SQL queries from Python
- Exception handling
- Lists and dictionaries
- DataFrame basics with Pandas
- GUI widgets and event binding
- Modular imports

## 📁 Project Structure

```text
python-cyber-crime-management/
│
├── README.md
│
├── app/
│   └── main.py
│
├── assets/
│   └── # application images/icons can be placed here
│
├── database/
│   └── # MySQL database/schema files can be placed here
│
├── screenshots/
│   └── # optional screenshots
│
└── demo/
    └── # optional project demo video
```

## ▶️ How to Run

1. Install Python 3.x.
2. Install the required packages:

```bash
pip install customtkinter mysql-connector-python pillow pandas
```

3. Create/configure the MySQL database used by the application.
4. Update the database connection settings in the Python code for your own computer.
5. Place required images/icons in the appropriate `assets` folder and update their paths if necessary.
6. Run the application:

```bash
python app/main.py
```

> **Security note:** Do not commit real database passwords, API keys, or other secrets to GitHub. Replace local credentials with environment variables or placeholders before publishing.

## 🎥 Project Demo

A short demonstration video can be added here to show:

- Login screen
- Dashboard
- Complaint registration
- Complaint search/view
- Chatbot
- Settings
- MySQL database interaction

**Demo video: Coming soon**

## 💼 Project Value

This project demonstrates practical Python skills in **GUI application development, database integration, CRUD-style workflows, user interaction, and application design**.

## 👨‍💻 Author

**Krishna KM**

Data Analyst | Excel | SQL | Python | Power BI
