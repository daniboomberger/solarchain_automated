from api.config import api_channel

class apiDataHandler():
    
    def __init__(self):
        self.consumption = []
        self.devices = []

    def handleDevices(self, data):
        device_names = []
        for device in data["header"]["epoch_devices"]:
            epoch = device

        names = data["header"]["epoch_devices"][epoch]
        for i in range(0, len(names) - 2):
            device_names.append(names[str(i + 1)]["name"])
        
        self.devices = device_names

    def handleConsumption(self, data, street_name, time, end_time):
        string_time = str(time)
        device_counter = 0

        for entry in data["body"][string_time]:
            if device_counter < len(self.devices):
                consumption_amount = data["body"][string_time][entry][api_channel]
                apartment_consumption = [int(consumption_amount),
                                        self.devices[device_counter]]
                print(apartment_consumption)

        
