import logging
from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import override

from email_validator import EmailNotValidError, validate_email

from running_activity_analyzer.model import (
    ActivityDataDict,
    ActivityType,
    RunnerDataDict,
)

logger = logging.getLogger(__name__)


@dataclass
class Validator[T: Mapping[str, object]]:
    required_keys: list[str] = field(default_factory=list)

    def validate(self, data: T) -> bool:
        if len(self.required_keys) == 0:
            return True
        return self.has_required_keys(data)

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
    def is_valid_date(date_value: str) -> bool:
        try:
            date.fromisoformat(date_value)
            return True
        except ValueError:
            return False


# TODO: Include record IDs in missing-key logs.
@dataclass
class RunnerDataDictValidator(Validator[RunnerDataDict]):
    def __post_init__(self) -> None:
        if not self.required_keys:
            self.required_keys = [
                "runner_id",
                "first_name",
                "last_name",
                "age",
                "email",
            ]

    @override
    def validate(self, data: RunnerDataDict) -> bool:
        if not super().validate(data):
            return False
        if not self.is_valid_email(data["email"]):
            logger.error("Invalid email for runner_id=%s", data["runner_id"])
            return False

        return True


# TODO: Include record IDs in missing-key logs.
@dataclass
class ActivityDataDictValidator(Validator[ActivityDataDict]):
    def __post_init__(self) -> None:
        if not self.required_keys:
            self.required_keys = [
                "activity_id",
                "runner_id",
                "date",
                "activity_type",
                "duration_minutes",
            ]

    @override
    def validate(self, data: ActivityDataDict) -> bool:
        if not super().validate(data):
            return False

        if not self.is_valid_value_of(data["activity_type"], ActivityType):
            logger.error(
                "Invalid activity_type for activity_id=%s: %s",
                data["activity_id"],
                data["activity_type"],
            )
            return False

        if not self.is_valid_date(data["date"]):
            logger.error(
                "Invalid date for activity_id=%s: %s",
                data["activity_id"],
                data["date"],
            )
            return False

        return True
