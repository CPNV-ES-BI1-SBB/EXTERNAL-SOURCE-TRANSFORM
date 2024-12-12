import pytest
from tests.initial_data_example import get_initial_data_example
from tests.transformated_data_example import transformated_data_example
from app.services.transform_builder import TransformBuilder

class TestTransformBuilder:

    def test_transform_builder_set_initial_station_success(self):
        # GIVEN
        data = get_initial_data_example()
        builder = TransformBuilder(data)

        # WHEN
        builder.set_initial_station()

        # THEN
        assert builder.get_transformed_data()["name"] == transformated_data_example()["name"]

    def test_transform_builder_set_departures_station_success(self):
        # GIVEN
        data = get_initial_data_example()
        builder = TransformBuilder(data)

        # WHEN
        builder.set_departures_station()

        # THEN
        assert builder.get_transformed_data()["departures"] == transformated_data_example()["departures"]

    def test_transform_builder_build_success(self):
        # GIVEN
        data = get_initial_data_example()
        builder = TransformBuilder(data)

        # WHEN
        result = builder.build()

        # THEN
        assert result == transformated_data_example()

