from dataclasses import dataclass
from typing import TypedDict
from enum import Enum
from datetime import date

class RunnerDataDict(TypedDict):
    runner_id: str
    first_name: str
    last_name: str
    age: int
    email: str


class ActivityDataDict(TypedDict):
    activity_id: str    
    runner_id: str
    date: str
    activity_type: str
    duration_minutes: int 

class ActivityType(Enum):
      RUNNING = 'Running'
      STRENGTH = 'Strength'
      PILATES = "Pilates"
      SWIMMING = "Swimming"

@dataclass
class Runner:
    runner_id: str
    first_name: str
    last_name: str
    age: int
    email: str

    def to_dict(self) -> RunnerDataDict:
          return{
                "runner_id": self.runner_id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age":  self.age,
                "email": self.email
          }

@dataclass
class Activity:
    activity_id: str    
    runner_id: str
    date: date
    activity_type: ActivityType
    duration_minutes: int 

    def to_dict(self) -> ActivityDataDict:
         return {
            "activity_id": self.activity_id,    
            "runner_id": self.runner_id,
            "date": self.date.isoformat(),
            "activity_type": self.activity_type.value,
            "duration_minutes": self.duration_minutes
         }