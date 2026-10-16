from datetime import date
from src.model import (Runner, Activity, ActivityType)
import pytest

@pytest.fixture
def runner1() -> Runner:
    return Runner(runner_id = "R001", first_name = "Anna", last_name="Kowalska", age=32, email="anna.kowalska@example.com" )

@pytest.fixture
def runner2() -> Runner:
    return Runner(runner_id="R002", first_name="Piotr", last_name="Nowak", age=41, email="piotr.nowak@example.com")

@pytest.fixture
def runner3() -> Runner:
    return Runner(runner_id="R003", first_name="Julia", last_name="Wiśniewska", age=27, email="julia.wisniewska@example.com")

@pytest.fixture
def runners(runner1: Runner, runner2: Runner, runner3:Runner) -> list[Runner]:
    return [runner1, runner2, runner3]

@pytest.fixture
def activity1() -> Activity:
    return Activity(activity_id="A001", runner_id="R001", date=date(2026, 9, 1), activity_type=ActivityType.RUNNING, duration_minutes=45)
    
@pytest.fixture
def activity2() -> Activity:    
    return Activity(activity_id="A002", runner_id="R001", date=date(2026, 9, 3), activity_type=ActivityType.PILATES, duration_minutes=50)    

@pytest.fixture
def activity3() -> Activity:
    return Activity(activity_id="A003", runner_id="R002", date=date(2026, 9, 2), activity_type=ActivityType.STRENGTH, duration_minutes=60)

@pytest.fixture
def activity4() -> Activity:
    return Activity(activity_id="A004", runner_id="R002", date=date(2026, 9, 5), activity_type=ActivityType.RUNNING, duration_minutes=35)

@pytest.fixture
def activity5() -> Activity:
    return Activity(activity_id="A005", runner_id="R003", date=date(2026, 9, 4), activity_type=ActivityType.SWIMMING, duration_minutes=40)

@pytest.fixture
def activities(activity1: Activity, activity2: Activity, activity3: Activity, activity4: Activity, activity5: Activity) -> list[Activity]:
    return [activity1, activity2, activity3, activity4, activity5]
