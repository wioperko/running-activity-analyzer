# Sports Activity Management and Analysis Application

## Project Goal

The goal of the project is to create an application for managing data about people and their sports activities.

The application will communicate with JSON files that store information about participants and their completed activities.

The project will be divided into the following layers:

* data models
* data validation
* data conversion
* repositories
* service layer
* testing

---

# Data Structure

### Participants

Each participant has:

* a unique ID
* first name
* last name
* date of birth
* email address

Example:

```json
{
    "participant_id": "P001",
    "first_name": "Anna",
    "last_name": "Kowalska",
    "birth_date": "1994-06-15",
    "email": "anna@example.com"
}
```

### Activities

Each activity has:

* a unique ID
* participant ID
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
    "participant_id": "P001",
    "date": "2026-09-15",
    "activity_type": "RUNNING",
    "duration_minutes": 52
}
```

## Data Organization

After retrieving the data from the JSON files, it will be processed into a structure that allows aggregation of the time spent by individual participants on specific activities.

Example structure:

```python
{
    participant: {
        ActivityType.RUNNING: 320,
        ActivityType.STRENGTH: 90,
        ActivityType.PILATES: 120,
    }
}
```

Here, `participant` represents an instance of the `Participant` class. The values represent the total number of minutes spent by a given participant on each activity type.

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
Validation
    ↓
Conversion
    ↓
Data models
    ↓
Service layer
    ↓
Aggregated results

Tests → cover all application layers
```

## Data Models

Models representing:

* `Participant`
* `Activity`

as well as an enum defining the activity type.

## Validation

Validation will include, among other things:

* valid IDs
* valid email addresses
* valid date of birth
* valid activity type
* duration between 1 and 1440 minutes
* valid relationship between participant and activity IDs

## Conversion

Data retrieved from JSON files will be converted into appropriate Python objects.

* ISO-formatted date strings will be converted into `date` objects.
* Activity type strings will be converted into `ActivityType` enum members.
* Other values will be represented according to the types defined in the domain models.

## Repositories

Repositories will be responsible for communicating with the JSON files and retrieving data.

Planned repositories:

* `ParticipantRepository`
* `ActivityRepository`

## Service Layer

The service layer will be responsible for business logic, primarily data aggregation.


```text
get_activity_duration_by_participant()
```

The service should make it possible to retrieve the total duration for each activity type for a given participant.

## Testing

Tests will cover the individual application layers:

* models
* validation
* conversion
* repositories
* service logic
