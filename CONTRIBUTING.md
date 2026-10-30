# Contributing

## Ground rules

- Keep this project's original work clearly separated from third-party code, data, and quotations.
- Do not copy code from `ziweiknows/ziwei-chart` (GPL-3.0) into this repository. It is reference-only unless maintainers approve a documented licensing change.
- Before considering code from `Renhuai123/ziwei-doushu`, audit the exact files and revision under MIT, preserve notices, and review its datasets independently. MIT code licensing does not automatically license datasets, documents, or chart examples.
- Add provenance and license metadata before adding any external data or substantial quotation.
- Keep school-specific logic isolated. Do not silently resolve contradictory conventions.
- Label unverified calculations as TODO/unverified and make placeholder functions fail explicitly.
- Do not add personal birth data to fixtures without informed permission and a clear redistribution basis; prefer synthetic fixtures.

## Rule changes

Every calculation change should include a rule record, the convention profile it applies to, source/revision details, boundary cases, and independently checked expected results. Tests establish implementation behavior, not universal astrological truth; document disagreements.

## Pull requests

Describe the behavior changed, evidence and sources used, test cases added, licensing/provenance review, and any unresolved convention choices. Keep changes focused and preserve the audit trail.

## Development setup

The initial package targets Python 3.11+. Packaging and automated checks will be added after the repository's first review. Do not claim checks passed unless they were actually run.
