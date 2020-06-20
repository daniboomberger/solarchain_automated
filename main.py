from database.database import database

db = database()

if __name__ == "__main__":
    db.connect()