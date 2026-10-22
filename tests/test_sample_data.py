from pathlib import Path

from src.converter import ActivityConverter
from src.file_service import ActivityJsonDataReader
from src.validator import ActivityDataDictValidator

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def test_sample_activities_are_valid_and_convertible() -> None:
    records = ActivityJsonDataReader().read(DATA_DIR / "activities.json")
    validator = ActivityDataDictValidator()
    converter = ActivityConverter()

    for record in records:
        assert validator.validate(record), record
        converter.convert(record)
