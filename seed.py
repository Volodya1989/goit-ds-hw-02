import random
import sqlite3

from faker import Faker

fake = Faker()

conn = sqlite3.connect("task_manager.db")
cursor = conn.cursor()

# Seed status table with predefined values
statuses = ["new", "in progress", "completed"]
for status in statuses:
    cursor.execute("INSERT OR IGNORE INTO status (name) VALUES (?)", (status,))


# Seed users
def seed_users(n=10):
    for _ in range(n):
        full_name = fake.name()
        email = fake.unique.email()
        cursor.execute(
            "INSERT INTO users (fullname, email) VALUES (?, ?)", (full_name, email)
        )


# Seed tasks
def seed_tasks(n=30):
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text() if random.random() > 0.2 else None
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute(
            """
            INSERT INTO tasks (title, description, status_id, user_id)
            VALUES (?, ?, ?, ?)
        """,
            (title, description, status_id, user_id),
        )


if __name__ == "__main__":
    seed_users()
    seed_tasks()
    conn.commit()
    conn.close()
    print("Database seeded successfully.")
