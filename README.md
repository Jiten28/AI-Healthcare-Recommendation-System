# 🩺 MediVerse AI – Healthcare Recommendation System

An AI-powered Healthcare Recommendation System built with **Flask**, **Machine Learning**, and **Bootstrap** that predicts diseases based on symptoms and provides medicine recommendations, doctor suggestions, healthcare analytics, and an admin dashboard.

---

## 🚀 Features

### 👤 User Authentication
- User Registration
- Secure Login
- Password Hashing (Flask-Bcrypt)
- Session Management (Flask-Login)

---

### 🤖 AI Disease Prediction

- Predict disease using Machine Learning
- Confidence score
- Prediction history
- Symptom-based diagnosis

---

### 💊 Medicine Recommendation

- AI-based medicine recommendation
- Disease-specific suggestions
- Recommendation generated after prediction

---

### 👨‍⚕️ Doctor Recommendation

Provides specialist recommendations such as:

- Cardiologist
- Neurologist
- Dermatologist
- Orthopedic
- Pediatrician
- Psychiatrist
- ENT Specialist
- Pulmonologist
- Gastroenterologist
- Gynecologist
- Endocrinologist
- Ophthalmologist

*(Future versions will include doctor contact details, location, hospital information, and appointment booking links.)*

---

### 📊 Healthcare Analytics

Interactive analytics dashboard including:

- Total Predictions
- Average Confidence
- Most Predicted Disease
- Prediction History
- Bar Chart
- Pie Chart
- Line Chart

---

### 📈 Dashboard

Beautiful dashboard displaying

- Latest Prediction
- Disease Statistics
- Charts
- Prediction Summary

---

### 🛡 Admin Dashboard

Admin-only access

Features:

- Total Users
- Total Diseases
- Total Predictions
- Recent Activity
- Healthcare Statistics

Normal users cannot access the Admin Dashboard.

---

### 📄 Export Reports

Export prediction reports as:

- PDF Report
- Excel Report (.xlsx)

---

## 🛠 Tech Stack

### Backend

- Flask
- Flask SQLAlchemy
- Flask Login
- Flask Bcrypt
- WTForms

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js
- Jinja2

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy

### Database

- SQLite

### Report Generation

- ReportLab (PDF)
- OpenPyXL (Excel)

---

## 📂 Project Structure

```
AI-Healthcare-Recommendation-System
│
├── app
│   ├── forms
│   ├── models
│   ├── routes
│   ├── templates
│   ├── static
│   ├── ml
│   └── __init__.py
│
├── dataset
│
├── Document
│
├── instance
│
├── requirements.txt
├── config.py
├── run.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/Jiten28/AI-Healthcare-Recommendation-System.git
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Project

```bash
python run.py
```

---

Application will run on

```
http://127.0.0.1:5000/
```

---

## 📸 Screenshots

Add screenshots of

- Landing Page
- Login
- Dashboard
- Analytics
- Disease Prediction
- Medicine Recommendation
- Doctor Recommendation
- Admin Dashboard

---

## 🔮 Future Improvements

- AI Doctor Chatbot (Ollama)
- Hospital Finder
- Doctor Appointment Booking
- Doctor Contact Details
- Maps Integration
- Medical Report Upload
- Email Notifications
- Multi-language Support

---

## 📦 Requirements

See

```
requirements.txt
```

---

## 👨‍💻 Author

**Jiten Kumar**

LinkedIn:
*[(LinkedIn URL)](https://www.linkedin.com/in/jiten-kumar-85a03217a/)*

GitHub:
*[(GitHub URL)](https://github.com/Jiten28)*

Portfolio:
*[(Portfolio URL)](https://jitenkumarportfolio.netlify.app/)*

---

## 📜 License

This project is developed for educational and portfolio purposes.
