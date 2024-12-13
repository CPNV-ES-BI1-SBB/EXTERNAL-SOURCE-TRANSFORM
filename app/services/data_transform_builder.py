from app.errors.unable_to_process_error import UnableToProcessError


class DataTransformBuilder:
    def __init__(self, input: dict):
        self._input = input
        self._output = {}

    def build(self) -> dict:
        return self._output

    def set_initial_station(self):
        self._output["name"] = self._input["stop"]["name"]
        return self

    def set_departures(self):
        try:
            self._output["departures"] = [
                self._build_departure(connection) for connection in self._input["connections"]
            ]
            return self
        except KeyError:
            raise UnableToProcessError()

    def _build_departure(self, connection: dict) -> dict:
        try:
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
        except KeyError:
            raise UnableToProcessError()

    @staticmethod
    def _split_track(track: str) -> tuple:
        for index, char in enumerate(track):
            if char.isalpha():
                return track[:index], track[index:]
        return track, None