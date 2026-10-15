# Public GitHub Projects · Board Blueprint

**Status: native public GitHub Projects board created** at [Melissa Castro | Engineering Roadmap](https://github.com/users/Dicureck/projects/1); its `Engineering Board` view exists, but existing Issues and workflow columns are still being configured. This document records the correct next steps.

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

- [x] Public board URL exists: [Engineering Roadmap](https://github.com/users/Dicureck/projects/1) (public globe indicator visible in the GitHub interface).
- [ ] Five existing Issues are imported by URL, not recreated.
- [ ] Status fields accurately reflect shipped and unfinished work.
- [ ] Optional columns show repository, area and priority.
- [ ] Portfolio README and [public roadmap](https://dicureck.github.io/roadmap.html) link to the official board.
- [ ] Major status changes include a comment or CI/release link as evidence.

## Finish configuration of the existing board

Do **not** create another project. Open the existing [Engineering Board view](https://github.com/users/Dicureck/projects/1/views/2).

1. Clear the accidental `status:` filter with no value, then **Save** the view.
2. Use **Add item** (or the board's + control) to search for the existing `Dicureck/Dicureck` Issues #7–#11. Do not create duplicate draft items.
3. Group by Status and configure four status options if permitted: Backlog, In Progress, Verification, Published. If Github only offers Todo/In Progress/Done, preserve those until customized.
4. Suggested initial states: #8 and #9 Backlog; #7 and #10 In Progress; closed #11 Published.
5. Confirm that a signed-out visitor can view the public board and update any references to `/views/2` if the view URL changes.

[Public project](https://github.com/users/Dicureck/projects/1) · [Board view](https://github.com/users/Dicureck/projects/1/views/2)

**Integration boundary:** The board was created manually in GitHub by its owner; current connected actions cannot directly add/move native Projects v2 cards. The board itself is real; issue imports and statuses are not yet verified.

[← Public roadmap](../ROADMAP.md) · [Official Releases](releases.md)
