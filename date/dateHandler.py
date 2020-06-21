import datetime

class dateHandler():
    
    def getDate(self):
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)        
        end_yesterday = yesterday + datetime.timedelta(hours=23, minutes=59)
        string_date, string_datetime = self.dateToString(yesterday)        
        return yesterday, end_yesterday, string_date, string_datetime
    
    def dateToString(self, yesterday):
        string_date = datetime.datetime.strftime(yesterday,"%Y-%m-%d")
        string_datetime = datetime.datetime.strftime(yesterday, "%Y-%m-%d %H:%M:%S")
        return string_date, string_datetime
    
