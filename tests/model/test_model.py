from running_activity_analyzer.model import Activity, Runner


def test_runner_to_dict(runner1: Runner) -> None:

    data = runner1.to_dict()
    expected_data = {
        "runner_id": "R001",
        "first_name": "Anna",
        "last_name": "Kowalska",
        "age": 32,
        "email": "anna.kowalska@example.com",
    }
    assert data == expected_data


def test_activity_to_dict(activity1: Activity) -> None:

    data = activity1.to_dict()
    expected_data = {
        "activity_id": "A001",
        "runner_id": "R001",
        "date": "2026-09-01",
        "activity_type": "RUNNING",
        "duration_minutes": 45,
    }

    assert data == expected_data
