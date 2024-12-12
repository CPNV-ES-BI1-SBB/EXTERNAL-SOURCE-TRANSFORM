class TransformBuilder:
    def __init__(self, data):
        self.original_data = data
        self.transformed_data = {}
    def build(self):
        self.set_initial_station()
        self.set_departures_station()
        return self.transformed_data

    def set_initial_station(self):
        self.transformed_data["name"] = self.original_data["stop"]["name"]

    def set_departures_station(self):
        departures = []
        for connection in self.original_data["connections"]:
            departure = {}
            departure["departureStationName"] = self.original_data["stop"]["name"]
            departure["destinationStationName"] = connection["terminal"]["name"]
            departure["viaStationNames"] = [stop["name"] for stop in connection["subsequent_stops"]]
            departure["departureTime"] = connection["time"]
            departure["train"] = {
                "g": connection["*G"],
                "l": connection["*L"],
            }
            track, sector = self.split_track(connection["track"])
            departure["platform"] = track
            departure["sector"] = sector
            departures.append(departure)
        self.transformed_data["departures"] = departures

    def split_track(self, track):
        for index, char in enumerate(track):
            if char.isalpha():
                return track[:index], track[index:]
        return track, None

    def get_transformed_data(self):
        return self.transformed_data