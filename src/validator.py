from dataclasses import dataclass, field
from src.model import RunnerDataDict, ActivityDataDict, ActivityType
from typing import Type, override
from enum import Enum
from email_validator import validate_email, EmailNotValidError
from datetime import date
from collections.abc import Mapping
import logging
logging.basicConfig(level=logging.INFO)



@dataclass
class Validator[T: Mapping[str, object]]:
    required_keys: list[str] = field(default_factory=list)

    def validate(self, data:T) -> bool:
        if len(self.required_keys) == 0:
            return True
        return self.has_required_keys(data)

    def has_required_keys(self,data:T) -> bool:
        missing_keys = [key for key in self.required_keys if key not in data]

        if missing_keys:
            logging.error(f"Missing required keys: {missing_keys}")
            return False
        return True

        
    @staticmethod
    def is_positive(data: int | str) -> bool:
        return isinstance(data, int) and data > 0

    @staticmethod
    def is_valid_value_of(value: str, enum_class: Type[Enum]) -> bool:
        return value in [item.value for item in enum_class]

    @staticmethod
    def is_valid_email(email:str) -> bool:
        try:
            validate_email(email, check_deliverability = False)
            return True
        except EmailNotValidError as e:
            logging.error(str(e))
            return False

    @staticmethod
    def is_valid_date(date_value:str) -> bool:
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
            self.required_keys = ['runner_id', 'first_name', 'last_name', 'age', 'email']
    @override
    def validate(self, data: RunnerDataDict) -> bool:
        if not super().validate(data):
            return False
        if not self.is_valid_email(data['email']):
            logging.error(f"Invalid email for runner_id: {data['runner_id']}")
            return False
        
        return True

# TODO: Include record IDs in missing-key logs.
@dataclass
class ActivityDataDictValidator(Validator[ActivityDataDict]):

    def __post_init__(self) -> None:
        if not self.required_keys:
            self.required_keys = ["activity_id", "runner_id", "date", "activity_type","duration_minutes"]

    @override
    def validate(self, data: ActivityDataDict) -> bool:
        if not super().validate(data):
            return False
        
        if not self.is_valid_value_of(data['activity_type'], ActivityType):
            logging.error(
                f'Invalid activity_type for activity_id={data["activity_id"]}: '
                f'{data["activity_type"]}'
            )
            return False

        if not self.is_valid_date(data['date']):
            logging.error(
                f'Invalid date for activity_id={data["activity_id"]}: '
                f'{data["date"]}'
            )
            return False

        return True
    


