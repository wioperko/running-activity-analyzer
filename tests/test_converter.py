from datetime import date

import pytest

from running_activity_analyzer.converter import ActivityConverter, RunnerConverter
from running_activity_analyzer.model import (
    Activity,
    ActivityDataDict,
    ActivityType,
    Runner,
    RunnerDataDict,
)


@pytest.mark.parametrize(
    "data, runner",
    [
        (
            {
                "runner_id": "R001",
                "first_name": "Anna",
                "last_name": "Kowalska",
                "age": 32,
                "email": "anna.kowalska@example.com",
            },
            Runner(
                runner_id="R001",
                first_name="Anna",
                last_name="Kowalska",
                age=32,
                email="anna.kowalska@example.com",
            ),
        ),
        (
            {
                "runner_id": "R002",
                "first_name": "Piotr",
                "last_name": "Nowak",
                "age": 41,
                "email": "piotr.nowak@example.com",
            },
            Runner(
                runner_id="R002",
                first_name="Piotr",
                last_name="Nowak",
                age=41,
                email="piotr.nowak@example.com",
            ),
        ),
    ],
)
def test_runner_converter_from_json(data: RunnerDataDict, runner: Runner) -> None:

    converter = RunnerConverter()
    result = converter.convert(data)
    assert result.runner_id == runner.runner_id
    assert result.first_name == runner.first_name
    assert result.last_name == runner.last_name
    assert result.age == runner.age
    assert result.email == runner.email


@pytest.mark.parametrize(
    "data, activity",
    [
        (
            {
                "activity_id": "A001",
                "runner_id": "R001",
                "date": "2026-09-01",
                "activity_type": "RUNNING",
                "duration_minutes": 45,
            },
            Activity(
                activity_id="A001",
                runner_id="R001",
                date=date.fromisoformat("2026-09-01"),
                activity_type=ActivityType.RUNNING,
                duration_minutes=45,
            ),
        ),
        (
            {
                "activity_id": "A002",
                "runner_id": "R001",
                "date": "2026-09-03",
                "activity_type": "STRENGTH",
                "duration_minutes": 50,
            },
            Activity(
                activity_id="A002",
                runner_id="R001",
                date=date.fromisoformat("2026-09-03"),
                activity_type=ActivityType.STRENGTH,
                duration_minutes=50,
            ),
        ),
    ],
)
def test_activity_converter_from_json(
    data: ActivityDataDict, activity: Activity
) -> None:

    converter = ActivityConverter()
    result = converter.convert(data)
    assert result.activity_id == activity.activity_id
    assert result.runner_id == activity.runner_id
    assert result.date == activity.date
    assert result.activity_type == activity.activity_type
    assert result.duration_minutes == activity.duration_minutes
