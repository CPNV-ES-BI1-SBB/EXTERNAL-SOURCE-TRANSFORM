import pytest
from fastapi.testclient import TestClient
from app.main import app
from tests.data_example.transformated_data_example import get_transformated_data_example
from unittest.mock import patch
from tests.mocks.aws_provider_mock import AWSProviderMock


class TestTransform:

    @patch("app.services.cloud_provider_factory.CloudProviderFactory.get_cloud_provider")
    def test_transform_objects(self, mock_get_cloud_provider):
        # GIVEN
        awsProviderMock = AWSProviderMock()
        mock_get_cloud_provider.return_value = awsProviderMock

        with TestClient(app) as client:
            response = client.post("/objects/transform", json={
                "objects_URI": "aws://path/to/objects"
            })
            print(response.json())
            assert response.status_code == 200
            assert response.json() == get_transformated_data_example()


