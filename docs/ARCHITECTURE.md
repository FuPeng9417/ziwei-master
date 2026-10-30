# Architecture

## Status

This describes intended boundaries, not implemented chart behavior. All calculation modules remain TODO until a rule specification, source record, and independent reference cases have been reviewed.

## Planned layers

1. **Input and time normalization** — preserve the supplied civil time, IANA time-zone identifier, location, and provenance; derive UTC and true-solar-time candidates only after the method is specified and verified.
2. **Calendar adapter** — isolate Gregorian/lunar conversion and leap-month conventions behind a replaceable interface.
3. **Chart model** — typed representation for birth inputs, twelve palaces, stars, transformations, and time layers. The initial model must not imply that placements are calculated.
4. **Base chart engine** — palace and star placement with a named convention profile and reproducible calculation trace.
5. **School engines** — independent modules for San He, Fei Xing, Qin Tian Si Hua, and He Luo. Cross-school comparison consumes outputs; it does not silently merge rules.
6. **Time engine** — separately modeled decade, annual, monthly, daily, and (if specified) hourly layers.
7. **Evidence and provenance** — every rule records source, edition/revision, interpretation, status, applicability, and known disagreement.
8. **Skill interface** — request missing inputs, invoke only implemented deterministic calculations, and label unsupported areas as unverified.

## Data flow

`BirthInput` → validated input record → time candidates → convention-profiled chart request → calculation trace + chart result → optional school-specific analysis.

Each transformation should be explicit and retain its input. The system must be able to explain which time basis and convention profile produced each result.

## Boundaries

- No language-model inference may fill missing deterministic placements.
- A school module may consume shared chart facts but owns its interpretive rules.
- Source text and datasets are distinct from project code and carry separate rights metadata.
- No upstream implementation is copied in the scaffold.
