import urllib.request
import json
from api.config import api_url, api_modes, api_channel, api_credentials

class apiHandler():

    def createTargetUrl(self, date, street_name):
        target_url =  api_url + \
            "username=" + api_credentials[street_name][0] + \
            "&password=" + api_credentials[street_name][1] + \
            "&function=" + api_modes[1] + \
            "&solarlog=" + api_credentials[street_name][2] + \
            "&format=json&date=" + date
        return self.getData(target_url)         

    def getData(self, target_url):
        try:
            url = urllib.request.urlopen(target_url)
            data = json.loads(url.read().decode())
            return data
        except:
            print("failed to get data")
            
