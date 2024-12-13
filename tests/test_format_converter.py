import pytest
from tests.data_example.csv_data_example import get_csv_object_example
from tests.data_example.initial_data_example import get_initial_data_example
from tests.data_example.json_object_example import get_json_object_example
from app.services.format_converter import FormatConverter
from tests.data_example.xml_object_example import get_xml_object_example
from app.errors.unknown_format_error import UnknownFormatError

class TestFormatConverter:
    def test_format_converter_convert_json_success(self):
        # GIVEN
        data = get_json_object_example()
        converter = FormatConverter()

        # WHEN
        result = converter.convert(data)

        # THEN
        assert result == get_initial_data_example()

    def test_format_converter_convert_xml_success(self):
        # GIVEN
        data = get_xml_object_example()
        converter = FormatConverter()

        # WHEN
        result = converter.convert(data)

        # THEN
        assert result == get_initial_data_example()

    def test_format_converter_convert_csv_success(self):
        # GIVEN
        data = get_csv_object_example()
        converter = FormatConverter()

        # WHEN
        result = converter.convert(data)

        # THEN
        assert result == get_initial_data_example()

    def test_format_converter_convert_unknown_format_failure(self):
        # GIVEN
        data = {"type": "unknown", "raw": "unknown"}
        converter = FormatConverter()

        # WHEN
        with pytest.raises(UnknownFormatError):
            converter.convert(data)