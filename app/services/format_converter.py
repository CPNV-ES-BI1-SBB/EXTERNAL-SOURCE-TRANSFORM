import json
from app.errors import UnknownFormatError

class FormatConverter:
    def convert(self, stream: str, type: str) -> dict:
        if not self._is_valid_file_format(type): raise UnknownFormatError(f"Unknown format: {type}")
        return getattr(self, f"_convert_{type}")(stream)

    def _is_valid_file_format(self, type: str) -> bool:
        return type in ['json', 'xml', 'csv']

    def _convert_json(self, stream: str) -> dict:
        return json.loads(stream)