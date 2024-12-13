from app.services.data_transform_builder import DataTransformBuilder
from app.services.cloud_provider_factory import CloudProviderFactory
from app.services.cloud_provider import CloudProvider

class DataTransformDirector:
    @staticmethod
    def clean_station_departures(path: str) -> dict:
        data = DataTransformDirector._load(path)
        data_transform_builder = DataTransformBuilder(data)
        return data_transform_builder.set_initial_station().set_departures().build()

    @staticmethod
    def _initialize_cloud_provider(path: str) -> CloudProvider:
        return CloudProviderFactory.get_cloud_provider(path)

    @staticmethod
    def _load(path) -> dict:
        cloud_provider = DataTransformDirector._initialize_cloud_provider(path)
        return cloud_provider.download(path)