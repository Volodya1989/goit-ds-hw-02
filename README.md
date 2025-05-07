
# 📘 GOIT Data Science HW 2 — Task Management System with SQLite

## 📚 Description

This project implements a task management system using an SQLite database. The database consists of three main tables: `users`, `status`, and `tasks`. The schema ensures proper data organization, uniqueness of users and statuses, and cascading deletion of tasks when a user is removed.

## 📂 Project Structure

- `create_db.sql` — SQL script to create the database tables.
- `seed.py` — Python script for populating the database with test data using the `Faker` library.
- `queries.sql` — SQL queries required for the assignment (select, update, delete, aggregation).
- `requirements.txt` — List of Python dependencies.
- `README.md` — This file.

## 🛠️ Technologies Used

- Python 3.10+
- SQLite3
- Faker
- SQL

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Volodya1989/goit-ds-hw-02.git
cd goit-ds-hw-02
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## 🧱 Creating the Tables

Run the SQL script:

```bash
sqlite3 task_manager.db < create_db.sql
```

## 🌱 Populating the Database

Run the Python script:

```bash
python seed.py
```

## 🔍 Running SQL Queries

All required queries are in the `queries.sql` file. You can run them in the SQLite interactive shell:

```bash
sqlite3 task_manager.db
sqlite> .read queries.sql
```

## ✅ Implemented Features

- Table creation with appropriate constraints (`UNIQUE`, `FOREIGN KEY`, `ON DELETE CASCADE`).
- Generation of random users, statuses, and tasks.
- Queries including:
    - Selecting tasks by user or status.
    - Updating task statuses.
    - Finding users without any tasks.
    - Counting tasks.
    - Deleting tasks.
    - Filtering by email domain, etc.

## 👤 Author

**Volodymyr** [@Volodya1989](https://github.com/Volodya1989)
