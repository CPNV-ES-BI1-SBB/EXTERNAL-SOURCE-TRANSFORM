import pytest
from app.services.data_transform_director import DataTransformDirector
from tests.data_example.transformated_data_example import get_transformated_data_example
from tests.mocks.aws_provider_mock import AWSProviderMock


class TestDataTransformDirector:

    def test_data_transform_director_transform_data_success(self):
        # GIVEN
        awsProviderMock = AWSProviderMock("credentials")
        dataTransformDirector = DataTransformDirector(awsProviderMock)

        # WHEN
        result = dataTransformDirector.clean_station_departures("path")

        # THEN
        assert result == get_transformated_data_example()