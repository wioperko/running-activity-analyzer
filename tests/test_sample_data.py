from pathlib import Path
from typing import cast

from running_activity_analyzer.converter import (
    ActivityConverter,
    ParticipantConverter,
)
from running_activity_analyzer.file_service import (
    ActivityJsonDataReader,
    ParticipantJsonFileReader,
)
from running_activity_analyzer.model import ActivityDataDict, ParticipantDataDict
from running_activity_analyzer.validator import (
    ActivityDataDictValidator,
    ParticipantDataDictValidator,
    UniqueIdValidator,
)

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def test_sample_activities_are_valid_and_convertible() -> None:
    records = ActivityJsonDataReader().read(DATA_DIR / "activities.json")
    validator = ActivityDataDictValidator()
    converter = ActivityConverter()

    for record in records:
        result = validator.validate(record)
        assert result.is_valid, result.errors
        activity = converter.convert(cast(ActivityDataDict, record))
        assert activity.activity_id == record["activity_id"]

    unique_ids_result = UniqueIdValidator(field_name="activity_id").validate(records)

    assert unique_ids_result.is_valid, unique_ids_result.errors


def test_sample_participants_are_valid_and_convertible() -> None:
    records = ParticipantJsonFileReader().read(DATA_DIR / "participants.json")
    validator = ParticipantDataDictValidator()
    converter = ParticipantConverter()

    for record in records:
        result = validator.validate(record)
        assert result.is_valid, result.errors
        participant = converter.convert(cast(ParticipantDataDict, record))
        assert participant.participant_id == record["participant_id"]

    unique_ids_result = UniqueIdValidator(field_name="participant_id").validate(records)

    assert unique_ids_result.is_valid, unique_ids_result.errors
