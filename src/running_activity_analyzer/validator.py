import logging
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import ClassVar, override

from email_validator import EmailNotValidError, validate_email

from running_activity_analyzer.model import (
    ActivityDataDict,
    ActivityType,
    ParticipantDataDict,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class ValidationError:
    record_id: str | None
    field_name: str
    message: str


@dataclass(slots=True)
class ValidationResult:
    errors: list[ValidationError] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return not self.errors

    def add(self, record_id: str | None, field_name: str, message: str) -> None:
        self.errors.append(ValidationError(record_id, field_name, message))


@dataclass
@dataclass
class UniqueIdValidator:
    field_name: str

    def validate(
        self,
        records: Sequence[Mapping[str, object]],
    ) -> ValidationResult:
        result = ValidationResult()
        seen: set[str] = set()

        for record in records:
            value = record.get(self.field_name)

            if not isinstance(value, str):
                continue

            if value in seen:
                result.add(
                    record_id=value,
                    field_name=self.field_name,
                    message=f"Duplicate {self.field_name}: {value}",
                )
            else:
                seen.add(value)

        return result


@dataclass
class Validator[T: Mapping[str, object]]:
    required_keys: list[str] = field(default_factory=list)

    def validate(self, data: T) -> ValidationResult:
        result = ValidationResult()
        record_id = self.get_record_id(data)

        for key in self.required_keys:
            if key not in data:
                result.add(
                    record_id=record_id,
                    field_name=key,
                    message=f"Missing required key: {key}",
                )
        return result

    @staticmethod
    def get_record_id(data: Mapping[str, object]) -> str | None:
        for key in ("participant_id", "activity_id"):
            value = data.get(key)
            if isinstance(value, str):
                return value
        return None

    def has_required_keys(self, data: T) -> bool:
        missing_keys = [key for key in self.required_keys if key not in data]

        if missing_keys:
            logger.error("Missing required keys: %s", missing_keys)
            return False
        return True

    @staticmethod
    def is_positive(data: int | str) -> bool:
        return isinstance(data, int) and data > 0

    @staticmethod
    def is_int_in_range(value: object, minimum: int, maximum: int) -> bool:
        return (
            isinstance(value, int)
            and not isinstance(value, bool)
            and minimum <= value <= maximum
        )

    @staticmethod
    def is_valid_value_of(value: str, enum_class: type[Enum]) -> bool:
        return value in [item.value for item in enum_class]

    @staticmethod
    def is_valid_email(email: str) -> bool:
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            return False

    @staticmethod
    def parse_iso_date(value: object) -> date | None:
        if not isinstance(value, str):
            return None

        try:
            parsed_date = date.fromisoformat(value)
        except ValueError:
            return None

        if parsed_date.isoformat() != value:
            return None

        return parsed_date

    @staticmethod
    def is_valid_id(value: object, prefix: str) -> bool:
        if not isinstance(value, str):
            return False

        pattern = rf"{prefix}\d{{3,}}"
        return re.fullmatch(pattern, value) is not None


@dataclass
class ParticipantDataDictValidator(Validator[ParticipantDataDict]):
    def __post_init__(self) -> None:
        if not self.required_keys:
            self.required_keys = [
                "participant_id",
                "first_name",
                "last_name",
                "birth_date",
                "email",
            ]

    @override
    def validate(self, data: ParticipantDataDict) -> ValidationResult:
        result = super().validate(data)
        record_id = self.get_record_id(data)

        if "participant_id" in data and not self.is_valid_id(
            data["participant_id"], "P"
        ):
            result.add(
                record_id=record_id,
                field_name="participant_id",
                message="Invalid participant ID format",
            )

        if "email" in data and not self.is_valid_email(data["email"]):
            result.add(
                record_id=record_id,
                field_name="email",
                message="Invalid email address",
            )

        if "birth_date" in data:
            birth_date = self.parse_iso_date(data["birth_date"])

            if birth_date is None:
                result.add(
                    record_id=record_id,
                    field_name="birth_date",
                    message="Invalid birth date; expected YYYY-MM-DD",
                )
            elif birth_date > date.today():
                result.add(
                    record_id=record_id,
                    field_name="birth_date",
                    message="Birth date cannot be in the future",
                )

        return result


@dataclass
class ActivityDataDictValidator(Validator[ActivityDataDict]):
    MIN_DURATION_MINUTES: ClassVar[int] = 1
    MAX_DURATION_MINUTES: ClassVar[int] = 1440

    def __post_init__(self) -> None:
        if not self.required_keys:
            self.required_keys = [
                "activity_id",
                "participant_id",
                "date",
                "activity_type",
                "duration_minutes",
            ]

    @override
    def validate(self, data: ActivityDataDict) -> ValidationResult:
        result = super().validate(data)
        record_id = self.get_record_id(data)

        if "activity_id" in data and not self.is_valid_id(data["activity_id"], "A"):
            result.add(
                record_id=record_id,
                field_name="activity_id",
                message="Invalid activity ID format",
            )

        if "participant_id" in data and not self.is_valid_id(
            data["participant_id"], "P"
        ):
            result.add(
                record_id=record_id,
                field_name="participant_id",
                message="Invalid participant ID format",
            )

        if "activity_type" in data and not self.is_valid_value_of(
            data["activity_type"], ActivityType
        ):
            result.add(
                record_id=record_id,
                field_name="activity_type",
                message="Invalid activity_type",
            )

        if "date" in data:
            activity_date = self.parse_iso_date(data["date"])

            if activity_date is None:
                result.add(
                    record_id=record_id,
                    field_name="date",
                    message="Invalid activity date",
                )

            elif activity_date > date.today():
                result.add(
                    record_id=record_id,
                    field_name="date",
                    message="Activity date cannot be in the future",
                )

        if "duration_minutes" in data and not self.is_int_in_range(
            data["duration_minutes"],
            self.MIN_DURATION_MINUTES,
            self.MAX_DURATION_MINUTES,
        ):
            result.add(
                record_id=record_id,
                field_name="duration_minutes",
                message="Duration must be between 1 and 1440 minutes",
            )
        return result
