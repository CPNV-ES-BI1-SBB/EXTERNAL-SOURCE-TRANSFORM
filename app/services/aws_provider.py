from app.core.settings import settings
from app.services.cloud_provider import CloudProvider

class AWSProvider(CloudProvider):
    def __init__(self):
        super().__init__()
        self._credentials = settings.AWS_CREDENTIALS
        self._connect()

    def download(self, path: str) -> dict:
        pass

    def _connect(self):
        pass

    def _disconnect(self):
        pass