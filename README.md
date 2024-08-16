# django_expense_tracker_api

# Expense Tracker Application

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Project](#running-the-project)
5. [Project Structure](#project-structure)
6. [How the Project Works](#how-the-project-works)
7. [API Endpoints](#api-endpoints)
8. [Testing](#testing)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview
The Expense Tracker application is designed to help users manage and track their expenses efficiently. It consists of two main components:
- **Backend API (Django):** Manages data processing, database operations, and provides RESTful API endpoints.
- **Frontend (React):** Offers a user-friendly interface for tracking expenses, interacting with the backend, and visualizing data.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Node.js (version 18.x or higher)
- npm (version 6.x or higher)
- SQLite (default database for the Django backend)

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
- The `migrations` directory stores database migrations.

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

- **Authentication:** You can implement authentication (e.g., JWT) to secure these endpoints if needed.

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
