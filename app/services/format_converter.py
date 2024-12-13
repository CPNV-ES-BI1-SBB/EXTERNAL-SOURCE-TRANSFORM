import json
import xmltodict
from app.errors import UnknownFormatError

class FormatConverter:
    def convert(self, stream) -> dict:
        format_data = self._get_file_format(stream)
        return getattr(self, f"_convert_{format_data}")(stream['raw'])

    def _get_file_format(self, stream) -> str:
        if 'type' in stream and stream['type'] in ['json', 'xml', 'csv']:
            return stream['type']
        else:
            raise UnknownFormatError("Unknown format")

    def _convert_json(self, raw_data) -> dict:
        return json.loads(raw_data)