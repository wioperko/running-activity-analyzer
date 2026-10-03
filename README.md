# Sports Activity Management and Analysis Application

## Project Goal

The goal of the project is to create an application for managing data about people and their sports activities.

The project will be inspired by the structure and methodology of a project involving products, customers, and orders, but it will use a different domain and its own data aggregation rules.

The application will communicate with JSON files that store information about runners and their completed activities.

The project will be divided into the following layers:

* data models
* data validation
* data conversion
* repositories
* service layer
* testing

---

# Data Structure

### Runners

Each person has:

* a unique ID
* first name
* last name
* age
* email address

Example:

```json
{
    "runner_id": "R001",
    "first_name": "Anna",
    "last_name": "Kowalska",
    "age": 33,
    "email": "anna@example.com"
}
```

### Activities

Each activity has:

* a unique ID
* runner ID
* date
* activity type
* duration

The activity type will be defined as an `Enum`.

Example values:

* `RUNNING`
* `CYCLING`
* `SWIMMING`
* `STRENGTH`
* `PILATES`

Example:

```json
{
    "activity_id": "A001",
    "runner_id": "R001",
    "date": "2026-09-15",
    "activity": "RUNNING",
    "duration_minutes": 52.5
}
```

## Data Organization

After retrieving the data from the JSON files, it will be processed into a structure that allows aggregation of the time spent by individual runners on specific activities.

Example structure:

```python
{
    Runner("R001"): {
        Activity.RUNNING: 320,
        Activity.STRENGTH: 90,
        Activity.PILATES: 120
    }
}
```

The value represents the total number of minutes spent by a given runner on a given activity.

## Example Result

```text
Anna Kowalska

RUNNING: 320 min
STRENGTH: 90 min
PILATES: 120 min

-----------------

TOTAL: 530 min
```

---


# Planned Architecture

The project will be divided into the following layers.

```text
JSON files
    ↓
Repositories
    ↓
Conversion
    ↓
Data models
    ↓
Validation
    ↓
Services
    ↓
Aggregated results

Tests → cover all application layers
```

## Data Models

Models representing:

* `Runner`
* `Activity`

as well as an enum defining the activity type.

## Validation

Validation will include, among other things:

* valid IDs
* valid email addresses
* valid age
* valid activity type
* positive duration value
* valid relationship between runner and activity IDs

## Conversion

Data retrieved from JSON files will be converted into appropriate Python objects.

Numeric values for which precision is important will be represented using `Decimal`.

## Repositories

Repositories will be responsible for communicating with the JSON files and retrieving data.

Planned repositories:

* `RunnerRepository`
* `ActivityRepository`

## Service Layer

The service layer will be responsible for business logic, primarily data aggregation.


```text
get_activity_duration_by_runner()
```

The service should make it possible to retrieve the total duration for each activity type for a given runner.

## Testing

Tests will cover the individual application layers:

* models
* validation
* conversion
* repositories
* service logic
