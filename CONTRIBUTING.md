# Contribution Guidelines

Thanks for helping improve this repository.

This project now uses `README.md` as the single source of truth for datasets, benchmarks, surveys, and tooling. Keep additions concise, citable, and aligned with the existing seven-topic taxonomy.

## What To Update

When adding or editing an entry:

1. Update the matching section in [`README.md`](README.md).
2. Keep the dataset or benchmark name, year, and primary link consistent everywhere it appears.
3. Use exactly one primary topic entry per dataset, and use italic cross-links in other relevant topics.
4. Preserve the section ordering rule: flagship entries first, then newest to oldest.

## Entry Rules

- Prefer official dataset, project, paper, benchmark, or code links.
- Keep descriptions factual and compact.
- Use badges in this order when available: `arXiv`, `Site`/`Project`, `Code`, `🤗`.
- Do not create duplicate full entries for the same dataset across topics.
- If a resource is not ego-only, say so directly in the description.

## Benchmarks

- Add benchmarks in the `### Benchmarks built on these datasets` table inside the relevant topic section.
- Use short capability labels and point to the official challenge, benchmark, or project page.
- Keep benchmark rows sorted newest to oldest within the topic.

## Pull Requests

Before opening a PR, check:

1. The rendered Markdown still looks correct on GitHub.
2. Every new dataset has one primary topic and any needed cross-links.
3. Badge links resolve to official resources.
4. Section ordering and topic framing remain intact.
5. No removed legacy files or old navigation references are reintroduced.

## Code Of Conduct

Please be respectful and constructive in issues and pull requests.
