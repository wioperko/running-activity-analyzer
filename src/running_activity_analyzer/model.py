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


@dataclass(frozen=True, slots=True)
class Participant:
    participant_id: str
    first_name: str
    last_name: str
    birth_date: date
    email: str


@dataclass(frozen=True, slots=True)
class Activity:
    activity_id: str
    participant_id: str
    performed_on: date
    activity_type: ActivityType
    duration_minutes: int
