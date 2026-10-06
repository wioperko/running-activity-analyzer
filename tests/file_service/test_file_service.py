from src.file_service import RunnerJsonFileReader, ActivityJsonDataReader
import pytest

def test_file_reader_runner() -> None:
    reader = RunnerJsonFileReader()
    runners_data = [
        {"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"},
        {"runner_id":"R002", "first_name":"Piotr", "last_name":"Nowak", "age":41, "email":"piotr.nowak@example.com"},
        {"runner_id":"R003", "first_name":"Marta", "last_name":"Wiśniewska", "age":27, "email":"marta.wisniewska@example.com"}
    ]

    runners = reader.read('./data/runners.json')

    assert runners == runners_data    


def test_file_reader_runner_2(tmp_path) -> None:
    file = tmp_path /'runners_tests.json'

    file.write_text('[{"runner_id": "R001", "first_name": "Anna"}]', encoding="utf-8")

    reader = RunnerJsonFileReader()

    result = reader.read(file)

    assert result == [{"runner_id": "R001", "first_name": "Anna"}]

def test_file_reader_activity() -> None:
    reader = ActivityJsonDataReader()

    activity_data = [
        {"activity_id":"A001", "runner_id":"R001", "date": "2026-09-01", "activity_type": "RUNNING", "duration_minutes":45},
        {"activity_id":"A002", "runner_id":"R001", "date": "2026-09-03", "activity_type": "STRENGTH", "duration_minutes":50},
        {"activity_id":"A003", "runner_id":"R001", "date": "2026-09-05", "activity_type": "RUNNING", "duration_minutes":60},
        {"activity_id":"A004", "runner_id":"R002", "date": "2026-09-02", "activity_type": "RUNNING", "duration_minutes":55},
        {"activity_id":"A005", "runner_id":"R002", "date": "2026-09-04", "activity_type": "PILATES", "duration_minutes":45},
        {"activity_id":"A006", "runner_id":"R003", "date": "2026-09-01", "activity_type": "SWIMMING", "duration_minutes":40},
        {"activity_id":"A007", "runner_id":"R003", "date": "2026-09-06", "activity_type": "RUNNING", "duration_minutes":50},
        {"activity_id":"A008", "runner_id":"R001", "date": "2026-09-08", "activity_type": "PILATES", "duration_minutes":60}
    ]

    result = reader.read('./data/activities.json')

    assert activity_data == result

def test_file_reader_activity_2(tmp_path) -> None:
    file = tmp_path/'activity_tests.json'

    file.write_text('[{"activity_id":"A001", "runner_id":"R001", "date": "2026-09-01", "activity_type": "RUNNING", "duration_minutes":45}]', encoding='utf-8')

    reader = ActivityJsonDataReader()

    result = reader.read(file)

    assert result == [{"activity_id":"A001", "runner_id":"R001", "date": "2026-09-01", "activity_type": "RUNNING", "duration_minutes":45}]