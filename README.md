# ToDo_Django

# ToDo Django App with Email Verification

This Django project implements a to-do list app with both traditional username/password authentication and one-click email sign-in.

## Features

- Traditional signup/login with username and password  
- Email-based login with secure one-time verification link  
- Task management (add, edit, delete, list)  
- Authentication and authorization  
- Custom user model (`CustomUser`)  
- Email sending using Gmail SMTP  
- Environment variable management with `.env` file  

## Tech Stack

- Python 3.x  
- Django 5.2.1  
- SQLite  
- Gmail SMTP  
- HTML/CSS templates  

## Project Structure

```
ToDo_Django/
├── ToDo_Django/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/       
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/   
│   ├── edit_todo.html
│   ├── email_signin.html
│   ├── loginn.html
│   ├── signup.html
│   └── todopage.html
│
├── static/        
│   └── style.css
│
├── .gitignore
├── README.md
├── requirements.txt
├── db.sqlite3
├── manage.py
└── .env
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ToDo_Django
```

### 2. Create and activate virtual environment

```bash
python -m venv todoenv
source todoenv/bin/activate  # On Windows: todoenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

```env
EMAIL_VERIFICATION_URL=http://localhost:8000/accounts/verify-email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Access the app

- Traditional Signup/Login: `http://localhost:8000/`  
- Email Sign-in: `http://localhost:8000/accounts/emailsignin/`  
- Verification Link: `http://localhost:8000/accounts/verify-email/<uidb64>/<token>/`  

## Custom User Model

The app uses a custom user model defined in `accounts.models.CustomUser` and set in `settings.py` as:

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

## Notes

- Tasks are linked to users via:  
  ```python
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```
- One-time email token is generated via Django’s `PasswordResetTokenGenerator`  
- `.env` variables are loaded using `python-dotenv`  
- Gmail SMTP requires you to use an app password (not your actual email password)  

## License

This project is for learning and demo purposes only.
