from src.model import RunnerDataDict, ActivityDataDict
import json

class FileReader[T]:
    def read(self, filename: str) -> list[T]:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)


class RunnerJsonFileReader(FileReader[RunnerDataDict]):
    pass

class ActivityJsonDataReader(FileReader[ActivityDataDict]):
    pass