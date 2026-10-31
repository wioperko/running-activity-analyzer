from pathlib import Path

import pytest

from running_activity_analyzer.file_service import (
    ActivityJsonDataReader,
    FileReader,
    InvalidJsonFileError,
    ParticipantJsonFileReader,
)
from running_activity_analyzer.model import ActivityDataDict, ParticipantDataDict


def test_file_reader_participant(
    participants_file: Path, participants_data: list[ParticipantDataDict]
) -> None:
    reader = ParticipantJsonFileReader()
    runners = reader.read(participants_file)
    assert runners == participants_data


def test_file_reader_activity(
    activities_file: Path, activities_data: list[ActivityDataDict]
) -> None:
    reader = ActivityJsonDataReader()
    activities = reader.read(activities_file)
    assert activities == activities_data


def test_reader_rejects_list_without_json_objects(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text("[1, 2, 3]", encoding="utf-8")

    reader = FileReader()

    with pytest.raises(InvalidJsonFileError):
        reader.read(file_path)


def test_reader_raises_custom_error_for_invalid_json(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    reader = FileReader()

    with pytest.raises(InvalidJsonFileError):
        reader.read(file_path)
