import json
from pathlib import Path


class InvalidJsonFileError(Exception):
    pass


class FileReader:
    def read(self, filename: str | Path) -> list[dict[str, object]]:
        try:
            with open(filename, encoding="utf-8") as file:
                data: object = json.load(file)

        except (OSError, json.JSONDecodeError) as error:
            raise InvalidJsonFileError(f"Cannot read JSON file: {filename}") from error

        if not isinstance(data, list) or not all(
            isinstance(item, dict) for item in data
        ):
            raise InvalidJsonFileError(
                f"Expected a JSON array of objects in {filename}"
            )

        return data


class ParticipantJsonFileReader(FileReader):
    pass


class ActivityJsonDataReader(FileReader):
    pass
