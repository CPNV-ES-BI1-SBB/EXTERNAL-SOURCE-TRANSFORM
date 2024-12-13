from tests.data_example.json_object_example import get_json_object_example
from app.services.format_converter import FormatConverter

class AWSProviderMock:
    def __init__(self, credentials: str):
        self.data = get_json_object_example()
        self.formatConverter = FormatConverter()

    def download(self, path: str) -> dict:
        return self.formatConverter.convert(self.data)

    def connect(self):
        pass

    def disconnect(self):
        pass