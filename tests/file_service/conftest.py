import json
from pathlib import Path

import pytest

from running_activity_analyzer.model import ActivityDataDict, ParticipantDataDict


@pytest.fixture
def participants_data() -> list[ParticipantDataDict]:
    return [
        {
            "participant_id": "P001",
            "first_name": "Anna",
            "last_name": "Kowalska",
            "birth_date": "1994-06-15",
            "email": "anna.kowalska@example.com",
        },
        {
            "participant_id": "P002",
            "first_name": "Piotr",
            "last_name": "Nowak",
            "birth_date": "1984-06-15",
            "email": "piotr.nowak@example.com",
        },
        {
            "participant_id": "P003",
            "first_name": "Marta",
            "last_name": "Wiśniewska",
            "birth_date": "2000-06-15",
            "email": "marta.wisniewska@example.com",
        },
    ]


@pytest.fixture
def activities_data() -> list[ActivityDataDict]:
    return [
        {
            "activity_id": "A001",
            "participant_id": "P001",
            "date": "2026-09-01",
            "activity_type": "RUNNING",
            "duration_minutes": 45,
        },
        {
            "activity_id": "A002",
            "participant_id": "P001",
            "date": "2026-09-03",
            "activity_type": "STRENGTH",
            "duration_minutes": 50,
        },
        {
            "activity_id": "A003",
            "participant_id": "P001",
            "date": "2026-09-05",
            "activity_type": "RUNNING",
            "duration_minutes": 60,
        },
        {
            "activity_id": "A004",
            "participant_id": "P002",
            "date": "2026-09-02",
            "activity_type": "RUNNING",
            "duration_minutes": 55,
        },
        {
            "activity_id": "A005",
            "participant_id": "P002",
            "date": "2026-09-04",
            "activity_type": "PILATES",
            "duration_minutes": 45,
        },
        {
            "activity_id": "A006",
            "participant_id": "P003",
            "date": "2026-09-01",
            "activity_type": "SWIMMING",
            "duration_minutes": 40,
        },
        {
            "activity_id": "A007",
            "participant_id": "P003",
            "date": "2026-09-06",
            "activity_type": "RUNNING",
            "duration_minutes": 50,
        },
        {
            "activity_id": "A008",
            "participant_id": "P001",
            "date": "2026-09-08",
            "activity_type": "PILATES",
            "duration_minutes": 60,
        },
    ]


@pytest.fixture
def participants_file(
    tmp_path: Path, participants_data: list[ParticipantDataDict]
) -> Path:
    file_path = tmp_path / "participants_tests.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(participants_data, file, ensure_ascii=False)
    return file_path


@pytest.fixture
def activities_file(tmp_path: Path, activities_data: list[ActivityDataDict]) -> Path:
    file_path = tmp_path / "activity_tests.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(activities_data, file, ensure_ascii=False)
    return file_path
