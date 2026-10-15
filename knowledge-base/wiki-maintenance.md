# Wiki & Documentation Maintenance

**Canonical source:** the Markdown guides under [knowledge-base/](https://github.com/Dicureck/Dicureck/tree/main/knowledge-base).

**Native Wiki:** [GitHub Wiki](https://github.com/Dicureck/Dicureck/wiki) uses a separate repository behind GitHub's Wiki feature. Changes to the knowledge base do **not** automatically appear as edits to native Wiki pages.

## How navigation is organized

- The profile README links to canonical guides and labs.
- This index organizes all technical subjects and the project roadmap.
- The native Wiki sidebar may link directly to canonical pages.
- Native Wiki pages can serve as readable summaries, but must be updated separately if copied.

## Editorial standards

1. Write for an engineer encountering the problem for the first time.
2. Introduce preconditions and known limitations near the beginning.
3. Make runnable snippets standalone or clearly mark them illustrative.
4. Use synthetic records and neutral object names.
5. Keep external behavior (email send, deployment, DML) opt-in and reviewed.
6. Distinguish offline unit tests from integration or production evidence.
7. Check relative links whenever pages move or are renamed.

## Wiki pages that already exist

The user-authored native [Home](https://github.com/Dicureck/Dicureck/wiki/Home), [SQL Performance](https://github.com/Dicureck/Dicureck/wiki/SQL-Performance) and sidebar are separate from this repository. Treat the native Wiki as a navigation portal while canonical technical notes remain in `knowledge-base/`. Do not assume template files automatically update the Wiki.

**Curated templates:** [Home](../wiki-starter/Home.md) · [Sidebar](../wiki-starter/_Sidebar.md) · [Database Migration](../wiki-starter/Database-Migration.md) · [Data Quality](../wiki-starter/Data-Quality.md). These are source-controlled proposals, **not proof of native Wiki publication**.

## Publishing cadence

Documentation updates can be reviewed in a GitHub commit. Native Wiki changes require a separate GitHub Wiki editor or an authorized browser/Git workflow; this project does not claim the two repositories are automatically synced.

[Home](README.md) · [Roadmap](portfolio-roadmap.md).

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*
