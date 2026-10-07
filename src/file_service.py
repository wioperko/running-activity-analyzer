from src.model import RunnerDataDict, ActivityDataDict
from pathlib import Path
import json

class FileReader[T]:
    def read(self, filename: str | Path) -> list[T]:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)


class RunnerJsonFileReader(FileReader[RunnerDataDict]):
    pass

class ActivityJsonDataReader(FileReader[ActivityDataDict]):
    pass


class FileWriter[T]:
    def write(self, filename: str | Path, data: list[T]) -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file,  ensure_ascii=False, indent=4)

class RunnerJsonFileWriter(FileWriter[RunnerDataDict]):
    pass

class ActivityJsonDataWriter(FileWriter[ActivityDataDict]):
    pass