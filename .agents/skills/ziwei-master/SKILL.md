---
name: ziwei-master
description: Work on the ZIWEI MASTER Zi Wei Dou Shu project. Use when designing, implementing, reviewing, or documenting this project's chart engine, time handling, school modules, provenance, or test fixtures.
---

# ZIWEI MASTER project skill

## Current implementation status

This repository is scaffolding. Treat all astrology calculations as unverified/TODO unless a module and its rule record explicitly say otherwise. Never invent a chart or imply that placeholder code has calculated one.

## Working rules

- Maintain the dual-time design: distinguish birth-place civil time from true solar time and state the method and source for any conversion.
- Keep San He, Fei Xing, Qin Tian Si Hua, and He Luo rules isolated. Report cross-school agreements and disagreements separately.
- For every deterministic rule, record the convention, source/version, applicability, review status, and checked fixtures.
- Ask for missing birth inputs rather than guessing. Preserve uncertainty in date, time, location, time zone, and historical daylight-saving data.
- Do not use language-model intuition for placements that require calculation.
- For unsupported functions, say they are not implemented and do not provide fabricated results.
- Preserve licensing boundaries: no code copying from GPL-3.0 `ziweiknows/ziwei-chart`; audit MIT code and separately licensed data from `Renhuai123/ziwei-doushu` before any reuse. The current scaffold includes neither source's code nor data.

## Review checklist

1. Is the calculation implemented, or is it still TODO?
2. Is the convention profile explicit?
3. Are civil-time and true-solar-time paths distinguishable?
4. Is each school-specific claim attributed to its own rule set?
5. Are source and dataset rights documented?
6. Are the expected cases independently checked and distributable?
