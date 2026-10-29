from running_activity_analyzer.model import Activity, Participant


def test_participant_to_dict(participant1: Participant) -> None:

    data = participant1.to_dict()
    expected_data = {
        "participant_id": "P001",
        "first_name": "Anna",
        "last_name": "Kowalska",
        "birth_date": "1994-06-15",
        "email": "anna.kowalska@example.com",
    }
    assert data == expected_data


def test_activity_to_dict(activity1: Activity) -> None:

    data = activity1.to_dict()
    expected_data = {
        "activity_id": "A001",
        "participant_id": "P001",
        "date": "2026-09-01",
        "activity_type": "RUNNING",
        "duration_minutes": 45,
    }

    assert data == expected_data
