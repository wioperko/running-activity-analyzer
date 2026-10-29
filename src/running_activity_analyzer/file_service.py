import json
from pathlib import Path

from running_activity_analyzer.model import ActivityDataDict, ParticipantDataDict


class FileReader[T]:
    def read(self, filename: str | Path) -> list[T]:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                raise ValueError(f"Expected a JSON array in {filename}")

        return data


class ParticipantJsonFileReader(FileReader[ParticipantDataDict]):
    pass


class ActivityJsonDataReader(FileReader[ActivityDataDict]):
    pass
