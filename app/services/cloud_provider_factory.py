from app.services.aws_provider import AWSProvider
from app.services.cloud_provider import CloudProvider

class CloudProviderFactory:
    @staticmethod
    def get_cloud_provider(path: str) -> CloudProvider:
        if path.startswith("aws://"):
            return AWSProvider()
        else:
            raise ValueError(f"Invalid cloud provider for path: {path}")


