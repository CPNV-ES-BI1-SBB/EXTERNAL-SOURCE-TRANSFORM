from tests.data_example.initial_data_example import get_initial_data_example
from tests.data_example.transformated_data_example import get_transformated_data_example
from app.services.data_transform_builder import DataTransformBuilder

class TestDataTransformBuilder:

    def test_data_transform_builder_set_initial_station_success(self):
        # GIVEN
        data = get_initial_data_example()
        builder = DataTransformBuilder(data)

        # WHEN
        result = builder.set_initial_station().build()

        # THEN
        assert result["name"] == get_transformated_data_example()["name"]

    def test_data_transform_builder_set_departures_station_success(self):
        # GIVEN
        data = get_initial_data_example()
        builder = DataTransformBuilder(data)

        # WHEN
        result = builder.set_departures().build()

        # THEN
        assert result["departures"] == get_transformated_data_example()["departures"]

