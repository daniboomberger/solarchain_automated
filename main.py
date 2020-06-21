from database.database import database
from date.dateHandler import dateHandler
from api.apiHandler import apiHandler

#initializing used classes
db = database()
dateHandler = dateHandler()
apiHandler = apiHandler()

#date variables
start_date = ""
end_date = ""
string_date = ""
string_datetime = ""

#list of houses
street_names = ["Schaffhauserstrasse", "Hungerbergstrasse"]

if __name__ == "__main__":
    db.connect() 
    start_date, end_date, string_date, string_datetime = dateHandler.getDate()
    for i in range(0,len(street_names)):          
        data = apiHandler.createTargetUrl(string_date, street_names[i])