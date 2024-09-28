
# FastAPI Voucher Management System
This is a FastAPI project that manages vouchers with a MySQL database.

## Features

- Create, read, update, and delete vouchers
- Asynchronous database operations using SQLAlchemy
- Pydantic models for data validation
- CORS support for frontend integration
- Logging for error tracking

## Prerequisites

- Python 3.11 or higher
- MySQL database
- pip (Python package installer)

## Setup

### 1. Clone the Repository
	git clone https://github.com/yourusername/voucher-management.git
	cd voucher-management
### 2. Create a Virtual Environment
	python -m venv my_env
	source my_env/bin/activate  # On Windows use `my_env\Scripts\activate`
### 3. Install Dependencies
	pip install -r requirements.txt
### 4. Create a MySQL database
	CREATE DATABASE fastapi_db;
### 5. Configure your .env file
Create a `.env` file in the backend  directory with the following variables:
	DATABASE_URL=mysql+aiomysql://username:password@localhost/fastapi_db
	APP_NAME="Expenses Tracker"
	FRONTEND_HOST="http://localhost:5173"
	ENVIRONMENT="local"
### 6. Create a migration file
	alembic revision --autogenerate -m "Initial migration"
### 7. Apply the migration
	alembic upgrade head
### 8. Run the Application
	uvicorn app.main:app --reload
### 9. Access the API Documentation
	http://127.0.0.1:8000/docs
