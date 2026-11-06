from abc import ABC, abstractmethod
from datetime import date
from typing import override

from running_activity_analyzer.model import (
    Activity,
    ActivityDataDict,
    ActivityType,
    Participant,
    ParticipantDataDict,
)


class Converter[T, U](ABC):
    @abstractmethod
    def convert(self, data: T) -> U:
        pass


class ParticipantConverter(Converter[ParticipantDataDict, Participant]):
    @override
    def convert(self, data: ParticipantDataDict) -> Participant:
        return Participant(
            participant_id=data["participant_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=date.fromisoformat(data["birth_date"]),
            email=data["email"],
        )


class ActivityConverter(Converter[ActivityDataDict, Activity]):
    @override
    def convert(self, data: ActivityDataDict) -> Activity:
        return Activity(
            activity_id=data["activity_id"],
            participant_id=data["participant_id"],
            performed_on=date.fromisoformat(data["date"]),
            activity_type=ActivityType(data["activity_type"]),
            duration_minutes=data["duration_minutes"],
        )
