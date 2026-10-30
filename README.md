# ZIWEI MASTER

An independent, auditable Zi Wei Dou Shu research and chart-engine project. The project is planned around a dual-time chart workflow and separately specified San He, Fei Xing, Qin Tian Si Hua, and He Luo schools.

> **Status: scaffolding only.** No chart-calculation rules are implemented or validated yet. Outputs must not be treated as calculated charts until the relevant modules have verified rules and reference cases.

## Project goals

- Keep civil-time and true-solar-time chart inputs distinguishable and reproducible.
- Represent chart data with stable, documented schemas.
- Keep school-specific rules and interpretations isolated and traceable to sources.
- Record uncertainty, disagreements, and provenance for every adopted rule and dataset.
- Provide a Codex Skill that explains the project workflow without inventing calculations.

## Current contents

- `docs/ARCHITECTURE.md` — component boundaries and planned data flow.
- `docs/TECHNICAL_SPEC.md` — requirements, interfaces, and unverified areas.
- `CONTRIBUTING.md` — development and review rules.
- `LICENSES.md` — project licensing and upstream audit policy.
- `src/ziwei_master/` — Python package scaffolding; calculation entry points explicitly raise `NotImplementedError`.
- `.agents/skills/ziwei-master/SKILL.md` — project-specific Codex Skill.

## Development

Python 3.11 or later is the intended runtime. The first implementation phase will establish packaging, schemas, and deterministic test fixtures before any astronomical or astrological calculations are added. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Upstream references

This repository currently contains **no copied upstream source code or datasets**.

- [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu): prior review reports MIT-licensed code and separately licensed datasets. Audit the exact revision, all notices, and each dataset's terms before reuse. No dataset reuse is authorized by this note.
- [ziweiknows/ziwei-chart](https://github.com/ziweiknows/ziwei-chart): prior review reports GPL-3.0. Reference only; do not copy code or create a derivative unless a future licensing review explicitly approves that distribution model.

These are preliminary provenance notes from the referenced project review, not a substitute for a fresh file-by-file audit before any reuse.

## License

Project-authored scaffolding is offered under Apache-2.0; see [LICENSE](LICENSE). This does not relicense third-party materials. Dataset and reference-material rights are tracked separately under [LICENSES.md](LICENSES.md).
