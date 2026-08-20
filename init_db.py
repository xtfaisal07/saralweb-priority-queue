from database.db import Database

db = Database()

with open("database/schema.sql", "r") as f:
    db.execute(f.read())

print("Database initialized successfully!")
db.close()