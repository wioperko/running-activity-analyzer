from dataclasses import dataclass
from datetime import date
from enum import StrEnum
from typing import TypedDict


class ParticipantDataDict(TypedDict):
    participant_id: str
    first_name: str
    last_name: str
    birth_date: str
    email: str


class ActivityDataDict(TypedDict):
    activity_id: str
    participant_id: str
    date: str
    activity_type: str
    duration_minutes: int


class ActivityType(StrEnum):
    RUNNING = "RUNNING"
    CYCLING = "CYCLING"
    SWIMMING = "SWIMMING"
    STRENGTH = "STRENGTH"
    PILATES = "PILATES"


@dataclass(frozen=True)
class Participant:
    participant_id: str
    first_name: str
    last_name: str
    birth_date: date
    email: str

    def to_dict(self) -> ParticipantDataDict:
        return {
            "participant_id": self.participant_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat(),
            "email": self.email,
        }


@dataclass(frozen=True)
class Activity:
    activity_id: str
    participant_id: str
    performed_on: date
    activity_type: ActivityType
    duration_minutes: int

    def to_dict(self) -> ActivityDataDict:
        return {
            "activity_id": self.activity_id,
            "participant_id": self.participant_id,
            "date": self.performed_on.isoformat(),
            "activity_type": self.activity_type.value,
            "duration_minutes": self.duration_minutes,
        }
