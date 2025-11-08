# Workout Tracker

A Django REST API for tracking workouts, exercises, sessions, and performance analytics. Users can register, log workouts, log exercises, view progress reports, and track their fitness journey. Admins can manage exercises and view user progress.

URL: https://workout-tracker-xd79.onrender.com/docs
---

## Features

* User authentication (JWT tokens)
* User profiles with BMI calculation
* CRUD operations for workouts and exercises
* Workout session reports and analytics
* Progress tracking and performance metrics
* Admin-controlled exercise management

---

## API Endpoints

| Resource                        | Method           | Description                                                   |
| ------------------------------- | ---------------- | ------------------------------------------------------------- |
| `/api/auth/register/`           | POST             | Register a new user                                           |
| `/api/auth/login/`              | POST             | Obtain JWT token                                              |
| `/api/auth/refresh/`            | POST             | Refresh JWT token                                             |
| `/api/auth/logout/`             | POST             | Logout / invalidate token                                     |
| `/api/users/`                   | GET              | List all users (admin)                                        |
| `/api/users/<id>/profile/`      | GET              | Get a specific user's profile (admin)                         |
| `/api/me/`                      | GET/PATCH        | Get or update logged-in user's profile                        |
| `/api/exercises/`               | GET/POST         | List exercises (public) / create exercise (admin)             |
| `/api/exercises/<id>/`          | GET/PATCH/DELETE | Retrieve, update, or delete exercise (admin for PATCH/DELETE) |
| `/api/workouts/`                | GET/POST         | List or create user's workouts                                |
| `/api/workouts/<id>/`           | GET/PATCH/DELETE | Retrieve, update, or delete a specific workout                |
| `/api/workouts/<id>/exercises/` | GET/POST         | List or add exercises to a workout                            |
| `/api/workouts/<id>/report/`    | GET              | Get or generate a report for a workout                        |
| `/api/me/progress/`             | GET              | Get overall progress across workouts                          |
| `/api/report/id/report-exercises`      | GET              | List user-specific workout session exercises                  |

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Workout-Tracker.git
cd Workout-Tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root:

```env
DEBUG=True
SECRET_KEY=your-django-secret-key

DB_NAME=workout_db
DB_USER=postgres
DB_PASSWORD=passion4science
DB_HOST=db.txrqpwalsgbxtvuqwupz.supabase.co
DB_PORT=5432
```

> For production, set `DEBUG=False` and use secure secrets.

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` for admin access and `http://127.0.0.1:8000/api/` for API endpoints and `http://127.0.0.1:8000/docs/` for swagger docs.

---

## Optional: Deploy with PostgreSQL (Supabase)

1. Update your `.env` with Supabase credentials.
2. Add SSL mode in `settings.py`:

```python
DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}
```

3. Run migrations on the Supabase-hosted database.
4. Use any cloud service (Render, Heroku, Railway) to deploy your Django app.

---

## Technologies Used

* Django REST Framework
* PostgreSQL / Supabase
* Python 3.10+
* JWT Authentication

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

---

## License

MIT License © 2025 Favour Daniel
