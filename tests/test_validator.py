from enum import Enum

import pytest

from running_activity_analyzer.model import (
    ActivityDataDict,
    ActivityType,
    ParticipantDataDict,
)
from running_activity_analyzer.validator import (
    ActivityDataDictValidator,
    ParticipantDataDictValidator,
    UniqueIdValidator,
    Validator,
)


@pytest.mark.parametrize(
    "value, expected",
    [
        (7, True),
        (0, False),
        (-8, False),
        ("5.5", False),
        ("aaa", False),
        ("0", False),
        ("-5.5", False),
    ],
)
def test_is_positive(value: int | str, expected: bool) -> None:
    assert Validator.is_positive(value) == expected


@pytest.mark.parametrize(
    "value, enum_class, expected",
    [
        ("RUNNING", ActivityType, True),
        ("SWIMMING", ActivityType, True),
        ("Running", ActivityType, False),
        ("Other", ActivityType, False),
        (" ", ActivityType, False),
    ],
)
def test_if_is_valid_value_of(
    value: str, enum_class: type[Enum], expected: bool
) -> None:
    assert Validator.is_valid_value_of(value, enum_class) == expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("valid@gmail.com", True),
        ("invalid-email.com", False),
        ("@missingusername.com", False),
        ("missingdomain@", False),
        ("user@nonexistentdomain.invalid", False),
    ],
)
def test_if_valid_email(email: str, expected: bool) -> None:
    assert Validator.is_valid_email(email) == expected


@pytest.mark.parametrize(
    "value, expected", [("2026-10-04", True), ("2026-02-30", False), ("abc", False)]
)
def test_is_valid_date(value: str, expected: bool) -> None:
    parsed_data = Validator.parse_iso_date(value)
    assert (parsed_data is not None) == expected


@pytest.mark.parametrize(
    "value, prefix, expected",
    [
        ("P001", "P", True),
        ("P1234", "P", True),
        ("P12345", "P", True),
        ("P01", "P", False),
        ("PABC", "P", False),
        ("R001", "P", False),
        ("A001", "A", True),
        ("A1234", "A", True),
        ("A01", "A", False),
        ("P001", "A", False),
        ("p001", "P", False),
        (" P001", "P", False),
        ("P001 ", "P", False),
        ("P001X", "P", False),
        (123, "P", False),
        (None, "P", False),
    ],
)
def test_test_is_valid_id(value: object, prefix: str, expected: bool) -> None:
    assert Validator.is_valid_id(value, prefix) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            {
                "participant_id": "P001",
                "first_name": "Anna",
                "last_name": "Kowalska",
                "birth_date": "1994-06-15",
                "email": "anna.kowalska@example.com",
            },
            True,
        ),
        (
            {
                "participant_id": "P002",
                "first_name": "Piotr",
                "last_name": "Nowak",
                "birth_date": "1984-06-15",
                "e": "piotr.nowak@example.com",
            },
            False,
        ),
    ],
)
def test_if_has_required_keys(data: ParticipantDataDict, expected: bool) -> None:
    required_keys = [
        "participant_id",
        "first_name",
        "last_name",
        "birth_date",
        "email",
    ]
    validator: Validator[ParticipantDataDict] = Validator(required_keys)
    assert validator.has_required_keys(data) == expected


@pytest.mark.parametrize(
    "required_keys, data, expected",
    [
        (
            [
                "participant_id",
                "first_name",
                "last_name",
                "birth_date",
                "email",
            ],
            {},
            False,
        ),
        ([], {}, True),
    ],
)
def test_validate_required_keys(
    required_keys: list[str], data: ParticipantDataDict, expected: bool
) -> None:
    validator: Validator[ParticipantDataDict] = Validator(required_keys)
    result = validator.validate(data)
    assert result.is_valid == expected, result.errors


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            {
                "participant_id": "P001",
                "first_name": "Anna",
                "last_name": "Kowalska",
                "birth_date": "1994-06-15",
                "email": "anna.kowalska@example.com",
            },
            True,
        ),
        (
            {
                "participant_id": "P001",
                "first_name": "Anna",
                "last_name": "Kowalska",
                "birth_date": 32,
            },
            False,
        ),
        (
            {
                "participant_id": "P001",
                "first_name": "Anna",
                "last_name": "Kowalska",
                "email": "anna.kowalska@example.com",
            },
            False,
        ),
        (
            {
                "participant_id": "P001",
                "first_name": "Anna",
                "birth_date": "1994-06-15",
                "email": "anna.kowalska@example.com",
            },
            False,
        ),
        (
            {
                "participant_id": "P001",
                "last_name": "Kowalska",
                "birth_date": 32,
                "email": "anna.kowalska@example.com",
            },
            False,
        ),
        (
            {
                "first_name": "Anna",
                "last_name": "Kowalska",
                "birth_date": "1994-06-15",
                "email": "anna.kowalska@example.com",
            },
            False,
        ),
    ],
)
def test_participants_data_dict_validator_missing_keys(
    data: ParticipantDataDict, expected: bool
) -> None:
    validator = ParticipantDataDictValidator()
    result = validator.validate(data)
    assert result.is_valid == expected, result.errors


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            {
                "activity_id": "A001",
                "participant_id": "P001",
                "date": "2026-09-01",
                "activity_type": "RUNNING",
                "duration_minutes": 45,
            },
            True,
        ),
        (
            {
                "activity_id": "A001",
                "participant_id": "P001",
                "date": "2026-09-01",
                "activity_type": "RUNNING",
            },
            False,
        ),
        (
            {
                "activity_id": "A001",
                "participant_id": "P001",
                "date": "2026-09-01",
                "duration_minutes": 45,
            },
            False,
        ),
        (
            {
                "activity_id": "A001",
                "participant_id": "P001",
                "activity_type": "RUNNING",
                "duration_minutes": 45,
            },
            False,
        ),
        (
            {
                "activity_id": "A001",
                "date": "2026-09-01",
                "activity_type": "RUNNING",
                "duration_minutes": 45,
            },
            False,
        ),
        (
            {
                "participant_id": "P001",
                "date": "2026-09-01",
                "activity_type": "RUNNING",
                "duration_minutes": 45,
            },
            False,
        ),
        (
            {
                "activity_id": "A001",
                "participant_id": "P001",
                "date": "2026-09-32",
                "activity_type": "RUNNING",
                "duration_minutes": 45,
            },
            False,
        ),
    ],
)
def test_activity_data_dict_validator(data: ActivityDataDict, expected: bool) -> None:
    validator = ActivityDataDictValidator()
    result = validator.validate(data)
    assert result.is_valid == expected, result.errors


@pytest.mark.parametrize(
    "participant_id",
    ["P01", "R001", "PABC"],
)
def test_participant_validator_rejects_invalid_id(
    participant_id: str,
) -> None:
    data: ParticipantDataDict = {
        "participant_id": participant_id,
        "first_name": "Anna",
        "last_name": "Kowalska",
        "birth_date": "1994-06-15",
        "email": "anna@example.com",
    }

    result = ParticipantDataDictValidator().validate(data)

    assert not result.is_valid
    assert any(error.field_name == "participant_id" for error in result.errors)


@pytest.mark.parametrize(
    "activity_id",
    ["A01", "P001", "AABC"],
)
def test_activity_validator_rejects_invalid_id(activity_id: str) -> None:
    data: ActivityDataDict = {
        "activity_id": activity_id,
        "participant_id": "P001",
        "date": "2026-09-01",
        "activity_type": "RUNNING",
        "duration_minutes": 45,
    }

    result = ActivityDataDictValidator().validate(data)

    assert not result.is_valid
    assert any(error.field_name == "activity_id" for error in result.errors)


@pytest.mark.parametrize(
    "participant_id",
    ["P01", "R001", "A001"],
)
def test_activity_validator_rejects_invalid_participant_id(
    participant_id: str,
) -> None:
    data: ActivityDataDict = {
        "activity_id": "A001",
        "participant_id": participant_id,
        "date": "2026-09-01",
        "activity_type": "RUNNING",
        "duration_minutes": 45,
    }

    result = ActivityDataDictValidator().validate(data)

    assert not result.is_valid
    assert any(error.field_name == "participant_id" for error in result.errors)


@pytest.mark.parametrize(
    "participant_ids, expected_error_count",
    [
        (["P001", "P002"], 0),
        (["P001", "P002", "P001"], 1),
        (["P001", "P001", "P001"], 2),
    ],
)
def test_validate_unique_participant_ids(
    participant_ids: list[str],
    expected_error_count: int,
) -> None:
    records = [{"participant_id": participant_id} for participant_id in participant_ids]

    result = UniqueIdValidator(field_name="participant_id").validate(records)

    assert len(result.errors) == expected_error_count
    assert result.is_valid == (expected_error_count == 0)


@pytest.mark.parametrize(
    "activity_ids, expected_error_count",
    [
        (["A001", "A002"], 0),
        (["A001", "A002", "A001"], 1),
        (["A001", "A001", "A001"], 2),
    ],
)
def test_validate_unique_activity_ids(
    activity_ids: list[str],
    expected_error_count: int,
) -> None:
    records = [{"activity_id": activity_id} for activity_id in activity_ids]

    result = UniqueIdValidator(field_name="activity_id").validate(records)

    assert len(result.errors) == expected_error_count
    assert result.is_valid == (expected_error_count == 0)
