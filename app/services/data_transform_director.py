from app.services.data_transform_builder import DataTransformBuilder

class DataTransformDirector:
    def __init__(self, awsProvider):
        self._awsProvider = awsProvider

    def clean_station_departures(self, path: str) -> dict:
        data = self._load(path)
        self._dataTransformBuilder = DataTransformBuilder(data)
        return self._dataTransformBuilder.set_initial_station().set_departures().build()

    def _load(self, path: str) -> dict:
        return self._awsProvider.download(path)
