# Project Decisions — Stage 1

> **Document status: draft for review.**
>
> This document consolidates the decisions made for Stage 1, their rationale, and their alignment with the current implementation. Decisions marked as requiring agreement have not yet been finalized.

## D1. Representation of activity types in JSON

**Decision:** Values of the `activity_type` field in JSON are written in uppercase, e.g. `"RUNNING"`. `ActivityType` is a `StrEnum`, and each member's value matches its name.

**Rationale:** A single, unambiguous format simplifies data validation and conversion. There is no need to handle multiple representations such as `"RUNNING"` and `"Running"`.

**Implementation status:** Consistent with the current model and sample data: `ActivityType` inherits from `StrEnum`, and the data uses values such as `"RUNNING"`.

## D2. List of activity types

**Decision:** The following five activity types are supported at this stage:

- `RUNNING`
- `CYCLING`
- `SWIMMING`
- `STRENGTH`
- `PILATES`

Adding another type requires an update to the specification.

**Rationale:** A closed set prevents unsupported values from being introduced accidentally and keeps the model, validation, data, and documentation consistent.

**Implementation status:** Consistent with the current `ActivityType` and README.

## D3. Duration type

**Decision:** Activity duration is stored as an `int` in minutes.

**Rationale:** The current logic uses whole minutes, so an integer type is sufficient for the chosen way of recording and aggregating duration.

**Implementation status:** Consistent with the current `ActivityDataDict`, the `Activity` model, and the sample data.

## D4. Duration range

**Decision:** The duration of a single activity must be between 1 and 1440 minutes, inclusive.

**Rationale:** Zero and negative values do not represent a completed activity, while the limit of 1440 minutes corresponds to one day.

**Implementation status:** The validator uses the constants `MIN_DURATION_MINUTES = 1` and `MAX_DURATION_MINUTES = 1440`. The `is_int_in_range` method also rejects values of type `bool`.

## D5. Participant date of birth

**Decision:** The participant model stores a `birth_date` field. In JSON, the date is represented as a string in `YYYY-MM-DD` format; in the domain object, it is a `datetime.date` object.

**Rationale:** Date of birth is a stable piece of information. Age can be calculated from the date of birth if needed.

**Implementation status:** Consistent with the `Participant` model, converter, and validator. Validation checks the date format and rejects dates of birth in the future.

## D6. ID Format

**Decision:** Participant IDs use the `P` prefix, and activity IDs use the `A` prefix:

- Participant ID: pattern `^P\d{3,}$`.
- Activity ID: pattern `^A\d{3,}$`.
- IDs must be unique within their respective data sets.

**Rationale:** Using distinct prefixes makes participant and activity identifiers easy to distinguish. Requiring at least three digits provides a consistent format while allowing the identifier space to grow. Sequential numbering is not required, so gaps in the numbering are allowed, and records do not need to appear in ID order in the JSON files.

**Implementation status:** ID format validation and duplicate ID detection have been implemented and tested. Sample data tests confirm that participant and activity IDs are valid and unique. Integration of dataset-level validation into the application processing flow remains pending until that flow is implemented.

## D7. Allowed activity dates

**Decision:** An activity date must use the exact `YYYY-MM-DD` format and must not be later than the date on which the application is run. Past dates are allowed.

**Rationale:** An exact format prevents ambiguous date interpretation, while disallowing future dates is consistent with the assumption that the stored activities have already taken place.

**Implementation status:** Consistent with the current validator: `parse_iso_date` checks the exact format, and the activity validator rejects future dates.

## D16. File Writing

**Decision:** Writing participant and activity records back to JSON files is outside the scope of Stage 1. The application will read JSON input files, validate and convert the data, and prepare it for aggregation and presentation.

**Rationale:** No specific use case has been identified that requires modified source records to be written back to JSON files. The existing `FileWriter`, `ParticipantJsonFileWriter`, and `ActivityJsonDataWriter` classes write lists of source records rather than aggregated reports.

**Separate point to consider:** Exporting aggregated results to a file may be useful in a later stage. This is different from writing source records and should be considered alongside decisions about output format (D14) and CLI arguments (D15). The feature may be introduced through a separate ADR when a concrete use case is identified.

**Implementation status:** Implemented. The writer classes and their related tests have been removed from Stage 1. JSON readers remain in place. Exporting aggregated results to a file is deferred to a later stage and may be considered through a separate ADR if a concrete use case arises.

## D17. Validation and conversion approach

**Decision:** For learning purposes, the project uses custom validation and conversion classes, along with a custom `ValidationResult`.

**Rationale:** Custom classes provide an opportunity to practise layer responsibilities, type annotations, error reporting, and testing.

**Implementation status:** Consistent with the chosen educational approach. The project has `ValidationResult`, `ValidationError`, validator classes, and separate converters.

## D18. Domain term for a person

**Decision:** The domain model consistently uses the term `Participant` rather than mixing `Runner`, `Athlete`, and `Participant`.

**Rationale:** Using one term simplifies the domain language and helps keep the names of classes, types, validators, converters, and documentation consistent.

**Implementation status:** The main classes and tests have been renamed to use `Participant`. The data file `data/runners.json` is planned to be renamed to `data/participants.json`, and all references to it should be updated.

---

## Summary before closing Stage 1

Before considering the stage consistent with these decisions, the following items must be resolved and/or implemented:

1. **D6:** Add validation for participant and activity ID patterns and uniqueness within the respective data sets.
2. **D16:** Confirm that writers for source records are excluded from Stage 1, or identify a specific use case that justifies retaining them. Consider saving aggregated results separately under D14/D15.
3. **D18:** Rename `data/runners.json` to `data/participants.json` and update all references.
4. After the decisions have been agreed, update the code, data, documentation, and tests, then rerun quality checks.

This document covers the decisions required in Step 2: D1–D7 and D16–D18. `docs/zalozenia.md` (Step 4) and `docs/specyfikacja.md` (Step 5) remain separate deliverables for later steps.
