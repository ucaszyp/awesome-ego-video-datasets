# Contribution Guidelines

Thanks for helping improve this repository.

This project is a curated index of egocentric video **datasets**, **benchmarks/challenges**, and **task-oriented** dataset views. Keep the three layers consistent: same names and years across files when the same resource appears in more than one place.

## What To Update

When adding or editing a **dataset**, update:

1. [`datasets.md`](datasets.md) (summary table + detailed entry)
2. The relevant file(s) under [`tasks/`](tasks/)
3. [`README.md`](README.md) only if the change affects the tools list or top-level navigation text

When adding or editing a **benchmark or challenge suite**, update:

1. [`benchmarks.md`](benchmarks.md) (place the row in the correct **year** section, newest first; within the year, sort by name)
2. [`datasets.md`](datasets.md) only if the benchmark introduces a **new** dataset corpus that should also be catalogued as data

## Repository Structure

- [`README.md`](README.md): navigation hub (surveys, links to datasets/benchmarks, tools)
- [`datasets.md`](datasets.md): dataset catalog only (summary + detailed entries)
- [`benchmarks.md`](benchmarks.md): benchmarks and official challenges using egocentric video
- [`tasks/`](tasks/): task-specific **dataset** views (not a second benchmark index)

## Dataset Entry Rules

### In `datasets.md`

Every dataset update should keep these two layers in sync:

1. The summary table near the top
2. The matching detailed entry in the long-form section

The summary table is a fast-scan layer. The detailed entries are the canonical reference for scale, paper, and download details.

### In `tasks/`

Add the dataset to every task view where it is genuinely useful. A dataset may appear in multiple task files.

Examples:

- Action datasets go in [`tasks/action-activity.md`](tasks/action-activity.md)
- QA / instruction datasets go in [`tasks/vlm-instruction-qa.md`](tasks/vlm-instruction-qa.md)
- Procedural datasets go in [`tasks/procedural-skill-learning.md`](tasks/procedural-skill-learning.md)

Do not force a dataset into a task file if the connection is weak.

## Year Convention

Use one year consistently across `README.md`, `datasets.md`, `benchmarks.md`, and `tasks/`:

- Default to the primary public discovery year used for readers to identify the resource
- Keep venue-specific timing details in the `Paper` field
- If a dataset and benchmark extension have different years, explain that in the detailed entry instead of mixing year conventions in headings

In practice, prefer consistency across repository views over trying to encode every release nuance in the title line.

## Scope And Taxonomy

When adding entries, be explicit about scope:

- `egocentric`: primarily first-person
- `ego+exo`: paired first- and third-person or multiview
- `not ego-only`: relevant to egocentric research, but not exclusively egocentric

If a resource is not ego-only, mark that clearly in the relevant row or note.

## Benchmark Rules

The benchmark index lives in [`benchmarks.md`](benchmarks.md).

Add a row only if it is one of these:

- A standalone benchmark with a clear evaluation setup and public splits or leaderboard
- A challenge suite or official benchmark hub (e.g. Ego4D, EPIC-KITCHENS challenges)
- A dataset release whose main use is a defined benchmark task (say so in the **Notes** column)

In the **Notes** column, tag entries as *Standalone*, *Suite*, or *Dataset+benchmark* (see [`benchmarks.md`](benchmarks.md) header).

## Formatting Rules

- Use official project, dataset, or paper links when possible
- Keep descriptions short and factual
- Sort summary-style tables by year descending unless the file already uses another documented convention
- Preserve existing Markdown table style
- Avoid marketing language

## Pull Requests

Before opening a PR, check:

1. The dataset name, year, and primary link are consistent across all touched files
2. You updated both the summary and detailed entry when changing `datasets.md`
3. You added task-file links only where they are clearly relevant
4. You updated `benchmarks.md` if the change adds or renames a benchmark; you updated `README.md` only if tools or top-level navigation change
5. The rendered Markdown tables still look correct

## Code Of Conduct

Please be respectful and constructive in issues and pull requests.
