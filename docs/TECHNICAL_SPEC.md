# Technical specification (initial)

## Scope

Build a Python library and Codex Skill for reproducible Zi Wei Dou Shu chart calculation and source-aware, school-separated research. The selected requirements are dual-time workflow, four school modules (San He, Fei Xing, Qin Tian Si Hua, He Luo), and a complete time-layer design.

## Non-goals for this scaffold

- Claiming a correct chart for any birth data.
- Implementing calendar conversion, true solar time, star placement, transformations, or interpretation before their conventions and test vectors are approved.
- Importing third-party source code, datasets, or copyrighted reference text.

## Initial interfaces

The package currently provides only placeholder types and functions. Planned public concepts:

- `BirthInput`: local civil datetime, IANA time-zone name, optional coordinates, and source/uncertainty metadata.
- `TimeBasis`: explicit civil-time or true-solar-time selection; both candidate charts may be requested together.
- `ConventionProfile`: named, versioned choices for calendar, day-boundary, leap-month, and other disputed conventions.
- `ChartRequest`: input, time basis, profile, and requested time layers.
- `ChartResult`: placements plus calculation trace, source/rule identifiers, and verification status.
- `RuleRecord`: rule text in project-authored terms, source citation, scope, review status, and tests.

These are design targets, not stable API guarantees.

## Verification gates

No calculation becomes `verified` until it has:

1. A precise convention statement and a named source or documented project decision.
2. Independently checked reference cases, including boundary cases relevant to that rule.
3. Deterministic tests with expected outputs and provenance for the expected values.
4. Review that confirms the test data may be redistributed.
5. A change log noting known disagreements and compatibility impact.

Until then, mark the rule `planned`, `under_review`, or `unverified`; do not present its output as authoritative.

## Planned phases

1. Finalize schema, input validation, and provenance model.
2. Select and verify calendar/time conversion conventions and fixtures.
3. Implement base chart placement with traceable rules.
4. Add each school as an isolated module with separate evidence and fixtures.
5. Add time layers in increasing scope, validating each independently.
6. Integrate the Skill with safe handling of unknown or unsupported calculations.
