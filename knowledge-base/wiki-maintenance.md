# Native GitHub Wiki | Protected Synchronization

**Status: Published and verified.** The [GitHub Actions run](https://github.com/Dicureck/Dicureck/actions/runs/38824211359) succeeded, including offline tests and a Git push to the separate Wiki repository.

The detailed source of truth remains [knowledge-base/](https://github.com/Dicureck/Dicureck/tree/main/knowledge-base). Eight hand-curated summaries under [wiki-pages/](https://github.com/Dicureck/Dicureck/tree/main/wiki-pages) are synchronized to the native [Engineering Wiki](https://github.com/Dicureck/Dicureck/wiki).

## Which pages are protected?

The original user-authored **[Home](https://github.com/Dicureck/Dicureck/wiki/Home)** and **[SQL Performance](https://github.com/Dicureck/Dicureck/wiki/SQL-Performance)** remain manually editable and are **never overwritten** by the workflow. Other existing pages are preserved too.

The Wiki sidebar keeps all handwritten text; the automation appends or refreshes **only the block between its two explicit START/END markers**.

## Automatically managed native tutorials

- [SQL Server → Oracle](https://github.com/Dicureck/Dicureck/wiki/Database-Migration)
- [Data Quality](https://github.com/Dicureck/Dicureck/wiki/Data-Quality)
- [Python & pandas](https://github.com/Dicureck/Dicureck/wiki/Python-Pandas)
- [Analytics Engineering](https://github.com/Dicureck/Dicureck/wiki/Analytics-Engineering)
- [AI & Business Automation](https://github.com/Dicureck/Dicureck/wiki/AI-Automation)
- [Enterprise Reporting / C#](https://github.com/Dicureck/Dicureck/wiki/Enterprise-Reporting)
- [BI Reporting Platforms](https://github.com/Dicureck/Dicureck/wiki/Reporting-Platforms)
- [Engineering Roadmap](https://github.com/Dicureck/Dicureck/wiki/Engineering-Roadmap)

## How edits work

To modify **Home** or **SQL Performance**, use GitHub's native Wiki editor as before.

To modify any of the **eight managed pages**, edit the corresponding Markdown document in [wiki-pages/](https://github.com/Dicureck/Dicureck/tree/main/wiki-pages) on the default branch. Changes trigger the [Wiki Sync workflow](https://github.com/Dicureck/Dicureck/actions/workflows/wiki-sync.yml). **Do not edit managed Wiki pages only in the Wiki UI**, because the next synchronization overwrites those sections.

The Python script [sync_wiki.py](https://github.com/Dicureck/Dicureck/blob/main/scripts/sync_wiki.py) edits an explicit file allowlist; it does not delete pages. Its unit tests preserve original content and confirm that repeated runs with unchanged files are idempotent. The workflow uses GitHub's repository-scoped Actions token, not a committed access key.

## Engineering publication standards

Document preconditions, observed evidence, explicit limitations, privacy-safe synthetic examples and links to tested code. Avoid treating standalone offline CI as proof of production integration.

[Canonical documentation](README.md) · [Public Board](https://github.com/users/Dicureck/projects/1/views/2) · [Verified first sync run](https://github.com/Dicureck/Dicureck/actions/runs/38824211359).
