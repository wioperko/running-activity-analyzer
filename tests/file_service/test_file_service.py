from pathlib import Path

from running_activity_analyzer.file_service import (
    ActivityJsonDataReader,
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
