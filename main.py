from database.database import database
from date.dateHandler import dateHandler

db = database()
dateHandler = dateHandler()

#date variables
start_date = ""
end_date = ""
string_date = ""
string_datetime = ""

if __name__ == "__main__":
    db.connect()
    start_date, end_date, string_date, string_datetime = dateHandler.getDate()    