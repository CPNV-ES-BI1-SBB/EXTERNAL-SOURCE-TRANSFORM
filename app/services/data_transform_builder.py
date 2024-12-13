class DataTransformBuilder:
    def __init__(self, data):
        self._input = data
        self._output = {}

    def build(self) -> dict:
        return self._output

    def set_initial_station(self):
        self._output["name"] = self._input["stop"]["name"]
        return self

    def set_departures(self):
        self._output["departures"] = [
            self._build_departure(connection) for connection in self._input["connections"]
        ]
        return self

    def _build_departure(self, connection) -> dict:
        departure = {
            "departureStationName": self._input["stop"]["name"],
            "destinationStationName": connection["terminal"]["name"],
            "viaStationNames": [stop["name"] for stop in connection["subsequent_stops"]],
            "departureTime": connection["time"],
            "train": {
                "g": connection["*G"],
                "l": connection["*L"],
            },
        }
        departure["platform"], departure["sector"] = self._split_track(connection["track"])
        return departure

    @staticmethod
    def _split_track(track) -> tuple:
        for index, char in enumerate(track):
            if char.isalpha():
                return track[:index], track[index:]
        return track, None