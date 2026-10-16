from src.model import RunnerDataDict, ActivityDataDict
from pathlib import Path
import json
import pytest


@pytest.fixture
def runners_data() -> list[RunnerDataDict]:
    return [
        {"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"},
        {"runner_id":"R002", "first_name":"Piotr", "last_name":"Nowak", "age":41, "email":"piotr.nowak@example.com"},
        {"runner_id":"R003", "first_name":"Marta", "last_name":"Wiśniewska", "age":27, "email":"marta.wisniewska@example.com"}
    ]

@pytest.fixture
def activities_data() -> list[ActivityDataDict]:
    return [
        {"activity_id":"A001", "runner_id":"R001", "date": "2026-09-01", "activity_type": "RUNNING", "duration_minutes":45},
        {"activity_id":"A002", "runner_id":"R001", "date": "2026-09-03", "activity_type": "STRENGTH", "duration_minutes":50},
        {"activity_id":"A003", "runner_id":"R001", "date": "2026-09-05", "activity_type": "RUNNING", "duration_minutes":60},
        {"activity_id":"A004", "runner_id":"R002", "date": "2026-09-02", "activity_type": "RUNNING", "duration_minutes":55},
        {"activity_id":"A005", "runner_id":"R002", "date": "2026-09-04", "activity_type": "PILATES", "duration_minutes":45},
        {"activity_id":"A006", "runner_id":"R003", "date": "2026-09-01", "activity_type": "SWIMMING", "duration_minutes":40},
        {"activity_id":"A007", "runner_id":"R003", "date": "2026-09-06", "activity_type": "RUNNING", "duration_minutes":50},
        {"activity_id":"A008", "runner_id":"R001", "date": "2026-09-08", "activity_type": "PILATES", "duration_minutes":60}
    ]

@pytest.fixture
def runners_file(tmp_path:Path, runners_data:list[RunnerDataDict]) -> Path:
    file_path = tmp_path/'runners_tests.json'
    with open(file_path, 'w') as file:
        json.dump(runners_data, file)
    return file_path


@pytest.fixture
def activities_file(tmp_path:Path, activities_data:list[ActivityDataDict]) -> Path:
    file_path = tmp_path/'activity_tests.json'
    with open(file_path, 'w') as file:
        json.dump(activities_data,file)
    return file_path
