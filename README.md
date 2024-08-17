# django_expense_tracker_api

# Expense Tracker Application

![Django API](https://github.com/thehamzza/django_expense_tracker_api/blob/main/api-django.png)

Live backend API: [https://django-expense-tracker-api.vercel.app/](https://django-expense-tracker-api.vercel.app/)

Live Web App: [https://react-expense-tracker-frontend.vercel.app/](https://react-expense-tracker-frontend.vercel.app/)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Project](#running-the-project)
5. [Project Structure](#project-structure)
6. [How the Project Works](#how-the-project-works)
7. [API Endpoints](#api-endpoints)
8. [Deployment](#deployment)
9. [Limitations and Future Improvements](#limitations-and-future-improvements)
10. [Testing](#testing)
11. [Contributing](#contributing)
12. [License](#license)

## Project Overview
The Expense Tracker application is designed to help users manage and track their expenses efficiently. It consists of two main components:
- **Backend API (Django):** Manages data processing, database operations, and provides RESTful API endpoints.
- **Frontend (React):** Offers a user-friendly interface for tracking expenses, interacting with the backend, and visualizing data.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Node.js (version 18.x or higher)
- npm (version 6.x or higher)
- PostgreSQL database (using Supabase)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Set Up the Backend:**

   - Navigate to the Django backend directory:
     ```bash
     cd django_expense_tracker
     ```

   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

   - Install the required Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```

   - Set up PostgreSQL on Supabase:
     - Sign up and create a project on [Supabase](https://supabase.com/).
     - Get your database connection URL and credentials (host, port, database, user, password).

   - Update your Django `settings.py` file with the PostgreSQL configuration:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': '<your-database-name>',
             'USER': '<your-database-username>',
             'PASSWORD': '<your-database-password>',
             'HOST': '<your-database-host>',
             'PORT': '<your-database-port>',
         }
     }
     ```

   - Run migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

   - (Optional) Create a superuser to access the Django admin panel:
     ```bash
     python manage.py createsuperuser
     ```

3. **Set Up the Frontend:**

   - Navigate to the React frontend directory:
     ```bash
     cd ../expense-tracker
     npm install
     ```

## Running the Project

1. **Run the Backend:**
   In the backend directory (`django_expense_tracker`), start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. **Run the Frontend:**
   In the frontend directory (`expense-tracker`), start the React development server:
   ```bash
   npm start
   ```
   
   The React app will be available at [http://localhost:3000](http://localhost:3000), and the backend API will be accessible at [http://localhost:8000](http://localhost:8000).

## Project Structure

### Backend (Django)
```
django_expense_tracker/
│
├── db.sqlite3
├── manage.py
├── django_expense_tracker/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│
└── transactions/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

### Frontend (React)
```
expense-tracker/
│
├── node_modules/
├── package.json
├── package-lock.json
├── public/
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── src/
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
└── README.md
```

## How the Project Works

### Backend (Django)
- The backend is a Django REST API that handles all CRUD operations for managing expenses. The `transactions` app manages the core business logic.
- The API is built using Django REST Framework (DRF) for serialization and viewsets.
- The PostgreSQL database is hosted on Supabase, ensuring robust data management and scalability.

### Frontend (React)
- The frontend is built using React and communicates with the backend through API requests. Axios is used for handling HTTP requests.
- The React app is designed to be responsive and provides an intuitive user experience.

## API Endpoints

| Endpoint                      | Method | Description                                  |
|-------------------------------|--------|----------------------------------------------|
| `/api/transactions/`          | GET    | Fetch all transactions                       |
| `/api/transactions/`          | POST   | Create a new transaction                     |
| `/api/transactions/<id>/`     | PUT    | Update an existing transaction               |
| `/api/transactions/<id>/`     | DELETE | Delete a transaction                         |

### Example API Testing Scenarios

#### 1. **Fetch All Transactions**
**Endpoint:** `GET /api/transactions/`

**Request:**
```bash
curl -X GET https://django-expense-tracker-api.vercel.app/api/transactions/
```

**Sample Response:**
```json
[
    {
        "id": 1,
        "type": "earning",
        "title": "hello",
        "amount": "12345.00",
        "date": "2024-08-16",
        "currency": "USD"
    },
    {
        "id": 2,
        "type": "expense",
        "title": "postgres",
        "amount": "1234.00",
        "date": "2024-08-16",
        "currency": "USD"
    },
    {
        "id": 5,
        "type": "earning",
        "title": "hamza testing 3",
        "amount": "123.00",
        "date": "2024-08-31",
        "currency": "USD"
    }
]
```

#### 2. **Create a New Transaction**
**Endpoint:** `POST /api/transactions/`

**Request:**
```bash
curl -X POST https://django-expense-tracker-api.vercel.app/api/transactions/ \
-H "Content-Type: application/json" \
-d '{
  "type": "expense",
  "title": "Utility Bill",
  "amount": "200.00",
  "date": "2024-09-01",
  "currency": "USD"
}'
```

**Sample Response:**
```json
{
    "id": 6,
    "type": "expense",
    "title": "Utility Bill",
    "amount": "200.00",
    "date": "2024-09-01",
    "currency": "USD"
}
```

#### 3. **Update an Existing Transaction**
**Endpoint:** `PUT /api/transactions/<id>/`

**Request:**
```bash
curl -X PUT https://django-expense-tracker-api.vercel.app/api/transactions/2/ \
-H "Content-Type: application/json" \
-d '{
  "type": "expense",
  "title": "Updated Postgres Test",
  "amount": "1250.00",
  "date": "2024-08-17",
  "currency": "USD"
}'
```

**Sample Response:**
```json
{
    "id": 2,
    "type": "expense",
    "title": "Updated Postgres Test",
    "amount": "1250.00",
    "date": "2024-08-17",
    "currency": "USD"
}
```

#### 4. **Delete a Transaction**
**Endpoint:** `DELETE /api/transactions/<id

>/`

**Request:**
```bash
curl -X DELETE https://django-expense-tracker-api.vercel.app/api/transactions/5/
```

**Sample Response:**
```json
{
    "message": "Transaction deleted successfully."
}
```

#### 5. **Fetch a Single Transaction**
**Endpoint:** `GET /api/transactions/<id>/`

**Request:**
```bash
curl -X GET https://django-expense-tracker-api.vercel.app/api/transactions/1/
```

**Sample Response:**
```json
{
    "id": 1,
    "type": "earning",
    "title": "hello",
    "amount": "12345.00",
    "date": "2024-08-16",
    "currency": "USD"
}
```

## Deployment

### Backend (Django)
The backend API is deployed on Vercel:
- URL: [https://django-expense-tracker-api.vercel.app/](https://django-expense-tracker-api.vercel.app/)

### Frontend (React)
The frontend is deployed on Vercel:
- URL: [https://react-expense-tracker-frontend.vercel.app/](https://react-expense-tracker-frontend.vercel.app/)

## Limitations and Future Improvements

**Current Limitation:**
- The app currently supports only a single user, meaning all expense data is shared and not isolated per user.

**Future Improvements:**
- Extend functionality to support multiple users with authentication, allowing each user to have their own separate database and transaction records.
- Implement user sign-up, login, and secure data isolation between users.

## Testing

To run tests for the Django backend:
```bash
python manage.py test
```
Tests are defined in the `tests.py` file located in the `transactions` app directory.

## Contributing
If you would like to contribute, feel free to open a pull request. Please follow the code style and guidelines specified in the project.

## License
This project is licensed under the MIT License.
