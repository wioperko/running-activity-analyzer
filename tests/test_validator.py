import pytest
from src.validator import Validator, RunnerDataDictValidator, ActivityDataDictValidator
from src.model import RunnerDataDict, ActivityType, ActivityDataDict
from enum import Enum
from typing import Type


@pytest.mark.parametrize('value, expected',[
    (7, True),
    (0, False),
    (-8,False),
    ("5.5", False),
    ("aaa", False),
    ("0", False),
    ("-5.5",False)
])
def test_is_positive(value: int |str , expected: bool) -> None:
    assert Validator.is_positive(value) == expected


@pytest.mark.parametrize('value, enum_class, expected',[
    ('RUNNING', ActivityType, True),
    ('SWIMMING', ActivityType, True),
    ('Running', ActivityType, False),
    ('Other', ActivityType, False),
    (' ', ActivityType, False)
])
def test_if_is_valid_value_of(value:str, enum_class:Type[Enum], expected: bool) -> None:
    assert Validator.is_valid_value_of(value, enum_class) == expected 

@pytest.mark.parametrize('email, expected',[
    ('valid@gmail.com', True),  
    ('invalid-email.com', False),  
    ('@missingusername.com', False), 
    ('missingdomain@', False), 
    ("user@nonexistentdomain.invalid", False)
])
def test_if_valid_email( email:str, expected:bool)-> None:
    assert Validator.is_valid_email(email) == expected


@pytest.mark.parametrize('value, expected',[
    ('2026-10-04', True),
    ('2026-02-30', False),
    ('abc', False)
])
def test_is_valid_date(value:str, expected: bool) -> None:
    assert Validator.is_valid_date(value) == expected

@pytest.mark.parametrize('data, expected',[
    ({"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"}, True),
    ({"runner_id":"R002", "first_name":"Piotr", "last_name":"Nowak", "age":41, "e":"piotr.nowak@example.com"}, False),
])
def test_if_has_required_keys(data:RunnerDataDict, expected: bool) -> None:
    required_keys = ["runner_id","first_name","last_name","age","email",]
    validator: Validator[RunnerDataDict] = Validator(required_keys)
    assert validator.has_required_keys(data) == expected

@pytest.mark.parametrize('required_keys, data, expected',[
    (["runner_id","first_name","last_name","age","email",], {}, False),
    ([], {}, True)

])
def test_validate_required_keys(required_keys:list[str], data:RunnerDataDict, expected: bool) -> None:
    validator: Validator[RunnerDataDict] = Validator(required_keys)
    assert validator.validate(data) == expected


@pytest.mark.parametrize('data, expected',[
    ({"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"}, True),
    ({"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32}, False),
    ({"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "email": "anna.kowalska@example.com"}, False),
    ({"runner_id" : "R001", "first_name" : "Anna", "age": 32, "email": "anna.kowalska@example.com"}, False),
    ({"runner_id" : "R001", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"}, False),
    ({"first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"}, False),
])
def test_runners_data_dict_validator_missing_keys(data:RunnerDataDict, expected: bool) -> None:
    validator = RunnerDataDictValidator()
    assert validator.validate(data) == expected


@pytest.mark.parametrize('data, expected', [
    ({"activity_id": "A001", "runner_id": "R001", "date": "2026-09-01", "activity_type": "RUNNING","duration_minutes": 45 }, True),
    ({"activity_id": "A001", "runner_id": "R001", "date": "2026-09-01", "activity_type": "RUNNING" }, False),
    ({"activity_id": "A001", "runner_id": "R001", "date": "2026-09-01", "duration_minutes": 45 }, False),
    ({"activity_id": "A001", "runner_id": "R001", "activity_type": "RUNNING","duration_minutes": 45 }, False),
    ({"activity_id": "A001", "date": "2026-09-01", "activity_type": "RUNNING","duration_minutes": 45 }, False),
    ({"runner_id": "R001", "date": "2026-09-01", "activity_type": "RUNNING","duration_minutes": 45 }, False),
    ({"activity_id": "A001", "runner_id": "R001", "date": "2026-09-32", "activity_type": "RUNNING","duration_minutes": 45 }, False),
])
def test_activity_data_dict_validator(data:ActivityDataDict, expected: bool) -> None:
    validator = ActivityDataDictValidator()
    assert validator.validate(data) == expected