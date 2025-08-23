# 🛠️ Backend - AI-Powered Quiz Application

The backend of the **Quiz Application**, built with **Django REST Framework (DRF)** and **PostgreSQL**.  
It provides APIs for user authentication, quiz generation, quiz attempts, and history tracking.

---

## 🚀 Tech Stack
- **Backend Framework**: Django REST Framework  
- **Database**: PostgreSQL  
- **Authentication**: JWT (SimpleJWT)  
- **AI Integration**: OpenAI / Gemini API  

---

## 📂 Project Structure
```
  backend/
│── quizproject/            # Django project root
│   │── __init__.py
│   │── settings.py
│   │── urls.py             # Root URL configuration
│   │── wsgi.py
│   │── asgi.py
│
│── authapp/                # Handles authentication
│   │── migrations/
│   │── __init__.py
│   │── models.py
│   │── views.py
│   │── urls.py
│   │── serializers.py
│   │── tests.py
│   │── admin.py
│   │── apps.py
│
│── quizapp/                # Core quiz logic
│   │── migrations/
│   │── __init__.py
│   │── models.py           # Quiz & Question models
│   │── serializers.py      # API serializers
│   │── views.py            # Quiz endpoints
│   │── urls.py             # Quiz URLs
│   │── ai.py               # AI integration for quiz generation
│   │── tests.py
│   │── admin.py
│   │── apps.py
│
│── manage.py               # Django management script
│── requirements.txt        # Dependencies
│── .gitignore
│── venv/                   # Virtual environment

```


---
## 🗄️ Database Design

The application uses **PostgreSQL** as the database. Below is the simplified schema.

### Entity Relationship Diagram (ERD)

User (Auth) 1 ──── ∞ Quiz 1 ──── ∞ Question

### Tables

#### User (Django built-in)
- id (PK)
- username
- email
- password
- ...

#### Quiz
- id (PK)
- user_id (FK → User.id)
- topic (varchar)
- difficulty (varchar: Easy/Medium/Hard)
- num_questions (int)
- completed (boolean)

#### Question
- id (PK)
- quiz_id (FK → Quiz.id)
- text (text)
- option_a (varchar)
- option_b (varchar)
- option_c (varchar)
- option_d (varchar)
- correct_option (varchar: A/B/C/D)

---
## API Endpoints
- POST /api/auth/register → Register user
- POST /api/auth/login → Login & get JWT
- POST /api/quiz/create → Generate quiz (AI)
- GET /api/quiz/take/<int:id> → Retrieve quiz
- POST /api/quizzes/user → Retrieve user quiz history
- GET /api/quiz/<int:id>/update-score/ → Update score

---

## ⚙️ Setup Instructions

### 1 Clone Repository
```bash
git clone https://github.com/your-username/quiz-app-backend.git
cd quiz-app-backend/backend
```
### 2️ Create Virtual Environment
```
  python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

```
### 3 Install Dependencies
```
  pip install -r requirements.txt

```
### 4 Setup Database
```
  CREATE DATABASE quiz_app;

```
### 5 Run Migrations
```
python manage.py migrate
```
### 6 Create Superuser
```
python manage.py createsuperuser

```
### 7 Start Server
```
python manage.py runserver

```

