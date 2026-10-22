import json
from pathlib import Path

from running_activity_analyzer.file_service import (
    ActivityJsonDataReader,
    ActivityJsonDataWriter,
    RunnerJsonFileReader,
    RunnerJsonFileWriter,
)
from running_activity_analyzer.model import ActivityDataDict, RunnerDataDict


def test_file_reader_runner(
    runners_file: Path, runners_data: list[RunnerDataDict]
) -> None:
    reader = RunnerJsonFileReader()
    runners = reader.read(runners_file)
    assert runners == runners_data


def test_file_reader_activity(
    activities_file: Path, activities_data: list[ActivityDataDict]
) -> None:
    reader = ActivityJsonDataReader()
    activities = reader.read(activities_file)
    assert activities == activities_data


def test_write_runners(tmp_path: Path, runners_data: list[RunnerDataDict]) -> None:
    writer = RunnerJsonFileWriter()
    file_path = tmp_path / "runners_tests.json"
    writer.write(file_path, runners_data)

    with open(file_path, encoding="utf-8") as file:
        saved_data = json.load(file)
    assert saved_data == runners_data


def test_write_ativity(tmp_path: Path, activities_data: list[ActivityDataDict]) -> None:
    writer = ActivityJsonDataWriter()
    file_path = tmp_path / "activities_tests.json"
    writer.write(file_path, activities_data)

    with open(file_path, encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == activities_data
