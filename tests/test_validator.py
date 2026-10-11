import pytest
from src.validator import Validator
from src.model import RunnerDataDict, ActivityType
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
def test_is_positive(value: int, expected: bool) -> None:
    assert Validator.is_positive(value) == expected


@pytest.mark.parametrize('value, enum_class, expected',[
    ('Running', ActivityType, True),
    ('Swimming', ActivityType, True),
    ('RUNNING', ActivityType, False),
    ('Other', ActivityType, False)
])
def test_if_is_valid_value_of(value:str, enum_class:Type[Enum], expected: bool) -> None:
    assert Validator.is_valid_value_of(value, enum_class) == expected 


@pytest.mark.parametrize('data, expected',[
    ({"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"}, True),
    ({"runner_id":"R002", "first_name":"Piotr", "last_name":"Nowak", "age":41, "e":"piotr.nowak@example.com"}, False),
])
def test_if_has_required_keys(data:RunnerDataDict, expected: bool) -> None:
    required_keys = ["runner_id","first_name","last_name","age","email",]
    validator = Validator(required_keys=required_keys)
    assert validator.has_required_keys(data) == expected

@pytest.mark.parametrize('required_keys, data, expected',[
    (["runner_id","first_name","last_name","age","email",], {"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"}, True),
    (["runner_id","first_name","last_name","age","email",], {"runner_id" : "R001"}, False),
    (["runner_id","first_name","last_name","age","email",], {}, False),
    ([], {}, True)

])
def test_with_not_all_keys(required_keys:list[str], data:RunnerDataDict, expected: bool) -> None:
    validator = Validator(required_keys)
    assert validator.validate(data) == expected