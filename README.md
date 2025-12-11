# 🔐 Password Strength Checker (Flask + Docker)

A simple and secure password analysis web application built with Python Flask.  
It checks password strength, identifies weaknesses, and provides recommendations.  
The application is fully containerized using Docker for easy deployment.

<img width="763" height="641" alt="image" src="https://github.com/user-attachments/assets/90a935ff-ff4b-4a3d-b7fe-6bf440945e0f" />


---

## 📌 Overview

This project demonstrates:

* A Flask web application  
* Password analysis logic (`password_utils.py`)  
* HTML templates  
* A production-ready Dockerfile  
* Port mapping for browser access  

It is ideal for cybersecurity beginners, Flask learners, and students building a portfolio project.

---

## 📂 Project Structure

```text
password-checker/
│
├── app.py                  # Flask server
├── password_utils.py       # Password analysis logic
├── templates/
│     └── index.html        # Frontend form UI
├── requirements.txt        # Python dependencies
└── Dockerfile              # Docker container instructions
