# 🌱 Seed Distribution App

A professional-grade application for environmental organizations (e.g., One Acre Fund) to efficiently register farmers and manage seed distribution in rural areas.

---

## 🌐 Tech Stack

- Django + Django REST Framework
- PostgreSQL
- JWT Authentication + User Roles
- Google Vision API (OCR - dropped for QR flow)
- React + Tailwind CSS (frontend)
- Raspberry Pi (deployment in home lab)

---

## 📦 Project Structure

| Folder/File     | Purpose                                      |
|------------------|----------------------------------------------|
| `backend/`       | Django app + API logic                      |
| `docs/`          | Technical diagrams, architecture, notes     |
| `scripts/`       | Deployment and automation scripts           |
| `.gitignore`     | Ignoring virtualenv, DB, etc.               |

---

## 🚀 Backend Setup

```bash
# Clone the repo
git clone https://github.com/bonheurNE07/seed-ditribution-app.git
cd backend

# Create and activate virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```
---

## 🔐 Authentication Flow

- JWT Login using email
- Step-by-step registration: email → code → password
- Roles via Django Groups: Admin, Agent
- Permission classes used in protected views

---

## 📊 API Endpoints Overview

```bash
- /api/dashboard/stats/ – Summary cards
- /api/dashboard/recent-farmers/
- /api/dashboard/recent-distributions/
- /api/dashboard/distribution-calendar/
- /api/farmers/, /api/species/, /api/distributions/ – Core modules
```
📌 Full API documentation coming soon via docs/.

---

## 📦 Deployment (Raspberry Pi - coming soon)

- Gunicorn + Nginx
- PostgreSQL on device
- Daily backup via shell script

---

## 👨‍💻 Author

Emmanuel Ndeze
Passionate software engineer focused on solving environmental and social challenges with code.
