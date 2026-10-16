from abc import abstractmethod, ABC
from typing import override
from datetime import date
from src.model import Runner, RunnerDataDict, Activity, ActivityDataDict, ActivityType

class Converter[T, U](ABC):
    @abstractmethod
    def convert(self,data:T) -> U:
        pass

class RunnerConverter(Converter[RunnerDataDict, Runner]):
    @override
    def convert(self, data:RunnerDataDict) -> Runner:
        return Runner (
            runner_id=data['runner_id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            age=data['age'],
            email= data['email']
        )

class ActivityConverter(Converter[ActivityDataDict, Activity]):
    @override
    def convert( self, data:ActivityDataDict) -> Activity:
        return Activity(
            activity_id=data['activity_id'],
            runner_id=data['runner_id'],
            date=date.fromisoformat(data['date']),
            activity_type=ActivityType(data['activity_type']),
            duration_minutes=data['duration_minutes']
        )
