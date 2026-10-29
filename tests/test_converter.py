from datetime import date

import pytest

from running_activity_analyzer.converter import ActivityConverter, ParticipantConverter
from running_activity_analyzer.model import (
    Activity,
    ActivityDataDict,
    ActivityType,
    Participant,
    ParticipantDataDict,
)


@pytest.mark.parametrize(
    "data, participant",
    [
        (
            {
                "participant_id": "P001",
                "first_name": "Anna",
                "last_name": "Kowalska",
                "birth_date": "1994-06-15",
                "email": "anna.kowalska@example.com",
            },
            Participant(
                participant_id="P001",
                first_name="Anna",
                last_name="Kowalska",
                birth_date=date(1994, 6, 15),
                email="anna.kowalska@example.com",
            ),
        ),
        (
            {
                "participant_id": "P002",
                "first_name": "Piotr",
                "last_name": "Nowak",
                "birth_date": "1984-06-15",
                "email": "piotr.nowak@example.com",
            },
            Participant(
                participant_id="P002",
                first_name="Piotr",
                last_name="Nowak",
                birth_date=date(1984, 6, 15),
                email="piotr.nowak@example.com",
            ),
        ),
    ],
)
def test_participant_converter_from_json(
    data: ParticipantDataDict,
    participant: Participant,
) -> None:

    converter = ParticipantConverter()
    result = converter.convert(data)
    assert result.participant_id == participant.participant_id
    assert result.first_name == participant.first_name
    assert result.last_name == participant.last_name
    assert result.birth_date == participant.birth_date
    assert result.email == participant.email


@pytest.mark.parametrize(
    "data, activity",
    [
        (
            {
                "activity_id": "A001",
                "participant_id": "P001",
                "date": "2026-09-01",
                "activity_type": "RUNNING",
                "duration_minutes": 45,
            },
            Activity(
                activity_id="A001",
                participant_id="P001",
                performed_on=date.fromisoformat("2026-09-01"),
                activity_type=ActivityType.RUNNING,
                duration_minutes=45,
            ),
        ),
        (
            {
                "activity_id": "A002",
                "participant_id": "P001",
                "date": "2026-09-03",
                "activity_type": "STRENGTH",
                "duration_minutes": 50,
            },
            Activity(
                activity_id="A002",
                participant_id="P001",
                performed_on=date.fromisoformat("2026-09-03"),
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
    assert result.participant_id == activity.participant_id
    assert result.performed_on == activity.performed_on
    assert result.activity_type == activity.activity_type
    assert result.duration_minutes == activity.duration_minutes
