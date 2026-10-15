# Public GitHub Projects · Board Blueprint

**Status: project configuration prepared, native GitHub Projects board not yet created.** This document is the source-controlled fallback until the owner opens GitHub's Projects interface and creates a project.

## Suggested GitHub Projects board

- **Title:** Melissa Castro | Engineering Roadmap
- **Description:** Public, verifiable progress on original data engineering, SQL, BI, Python and .NET demonstrations. Synthetic data only.
- **Visibility:** Public
- **Layout:** Board, grouped by the built-in Status field
- **Status columns:** Backlog → In Progress → Verification → Published

GitHub may name the default statuses "Todo / In Progress / Done". Rename/customize if the interface permits it. Use **Published** only after the code or evidence is publicly accessible.

## Import existing Issues

| Issue | Purpose | Suggested initial status |
|---|---|---|
| [#7 SQL Server deeper benchmark](https://github.com/Dicureck/Dicureck/issues/7) | Actual execution plans, logical reads and repeated trials | In Progress |
| [#8 BI native assets](https://github.com/Dicureck/Dicureck/issues/8) | Original Power BI/Tableau and paginated reports | Backlog |
| [#9 Cross-engine Oracle parity](https://github.com/Dicureck/Dicureck/issues/9) | Test controlled SQL Server and Oracle compatibility | Backlog |
| [#10 Wiki & native Projects](https://github.com/Dicureck/Dicureck/issues/10) | Native Wiki sync and this official board | In Progress |
| [#11 Official v0.1.0 Releases](https://github.com/Dicureck/Dicureck/issues/11) | Six published CI-gated releases | Published (completed) |

These items are already created in GitHub Issues. Do not duplicate them: add their **existing URLs** as items of the new project.

## Portfolio acceptance criteria

- [ ] Board has a public link readable without account access.
- [ ] Five existing Issues are imported by URL, not recreated.
- [ ] Status fields accurately reflect shipped and unfinished work.
- [ ] Optional columns show repository, area and priority.
- [ ] Portfolio README and [public roadmap](https://dicureck.github.io/roadmap.html) link to the official board.
- [ ] Major status changes include a comment or CI/release link as evidence.

## How to create the board

Open [your GitHub Projects overview](https://github.com/users/Dicureck/projects). Select **New project**, choose **Board**, give it the title above, and set visibility to **Public**. Use **Add item** to select existing `Dicureck/Dicureck` Issues #7–#11. Once the board exists, copy its official URL to update these documentation links.

**Why not already created?** The currently connected GitHub integration offers repository/files/actions/issues, but not a native user-owned Projects v2 creation/edit action. A Markdown roadmap is not misrepresented as a GitHub Projects board.

[← Public roadmap](../ROADMAP.md) · [Official Releases](releases.md)
