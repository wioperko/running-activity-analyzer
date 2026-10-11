from dataclasses import dataclass, field
from src.model import RunnerDataDict, ActivityDataDict
from typing import Type, override
from enum import Enum



@dataclass
class Validator[T]:
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
    def is_positive(data: int) -> bool:
        return isinstance(data, int) and data > 0

    @staticmethod
    def is_valid_value_of(value: str, enum_class: Type[Enum]) -> bool:
        return value in [item.value for item in enum_class]
 