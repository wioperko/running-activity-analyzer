from dataclasses import dataclass, field
from src.model import RunnerDataDict, ActivityDataDict, ActivityType
from typing import Type, override
from enum import Enum
from email_validator import validate_email, EmailNotValidError
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
       
        for key in self.required_keys:
            if key not in data:
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

@dataclass
class RunnerDataDictValidator(Validator[RunnerDataDict]):

    def __post_init__(self) -> None:
        if not self.required_keys:
            self.required_keys = ['runner_id', 'first_name', 'last_name', 'age', 'email']
    @override
    def validate(self, data: RunnerDataDict) -> bool:
        return super().validate(data) and self.is_valid_email(data['email'])

@dataclass
class ActivityDataDictValidator(Validator[ActivityDataDict]):

    def __post_init__(self) -> None:
        if not self.required_keys:
            self.required_keys = ["activity_id", "runner_id", "date", "activity_type","duration_minutes"]

    @override
    def validate(self, data: ActivityDataDict) -> bool:
        return super().validate(data) and self.is_valid_value_of(data['activity_type'], ActivityType)


