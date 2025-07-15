# Database Setup Guide

## Problem
You encountered a `KeyboardInterrupt` error when starting the FastAPI application. This happens because the application is trying to load database configuration from environment variables that don't exist.

## Solution

### 1. Create the `.env` file
Create a `.env` file in your project root directory with your actual database configuration:

```bash
# Copy env.example to .env
cp env.example .env
```

### 2. Configure your database settings
Edit the `.env` file with your actual database details:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=your_actual_database_name
DB_USER=your_actual_username
DB_PASSWORD=your_actual_password
```

### 3. Make sure your MySQL database is running
Ensure that your MySQL server is running and accessible with the credentials you provided.

### 4. Install dependencies (if needed)
```bash
pip install -r requirements.txt
```

### 5. Run the application
```bash
python run.py
```

## What was changed
- Added default values to `app/core/config.py` so the application won't crash immediately
- Added a warning message when the `.env` file is missing
- Created an `env.example` file as a template

## Next steps
1. Create your `.env` file with actual database credentials
2. Ensure your MySQL database exists and is accessible
3. Run the application again

The application should now start without the `KeyboardInterrupt` error. 