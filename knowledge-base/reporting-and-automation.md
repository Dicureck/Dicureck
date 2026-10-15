# Reporting Platforms, Software & AI Automation — Roadmap

These are **planned independent demonstrations**, not completed production case studies. The public repos linked below are the current reproducible evidence.

## Reporting & BI engineering

| Domain | Planned demonstrable artifact | Verification |
|:--|:--|:--|
| Tableau | Fictional operational incident trends and calculations | Public workbook or documented Tableau Public link, dataset, assumptions |
| Power BI | Star schema, DAX measures and refresh plan | [Logistics blueprint](https://github.com/Dicureck/logistics-route-intelligence/blob/main/docs/power-bi-blueprint.md) · [Finance blueprint](https://github.com/Dicureck/financial-intelligence-lab/blob/main/docs/power-bi-blueprint.md) |
| Crystal Reports | Fictional SQL-backed operational summary | Original template/report screenshots and source SQL without proprietary data |
| Report Builder / SSRS | Paginated financial & operational reports | Synthetic RDL, parameters, independent test data |

Software vendors' branding and proprietary binary project formats are not redistributed unless independently licensed and created with authorized tooling.

## Software engineering

**C# / .NET:** planned standalone CSV validation service with typed models, exceptions, CLI and tests. **JavaScript:** current evidence is the [Secret Friend browser app](https://github.com/Dicureck/challenge-amigo-secreto-esp_main). **Python + pandas:** reproducible labs for [Logistics](https://github.com/Dicureck/logistics-route-intelligence), [Finance](https://github.com/Dicureck/financial-intelligence-lab), and [Data Quality](https://github.com/Dicureck/data-quality-toolkit).

## Responsible AI-assisted workflows

- **AI-assisted web development:** original frontend code; use ChatGPT/Claude for drafting, then review and test every generated change. Do not imply an AI integration exists where there is only prompting.
- **Reusable prompt templates:** requirements discovery, SQL review, accessibility, test design, and documentation, with clear human verification steps. Do not publish private conversation transcripts.
- **Internal email/report automation:** mocked report scheduling, synthetic outbound messages, approval gates, dry-run mode and secretless local testing. Never send operational information to actual recipients by default.
- **Governance:** no customer prompts, database credentials, confidential documents, tokens, or real personal records. Track test coverage and known limitations.

## Current publication status

*Shipped*: the five original labs and apps linked from the [portfolio](https://github.com/Dicureck).

*Planned*: Tableau/Crystal/Report Builder examples, .NET/C# project, AI workflow samples, email automation, and operational incident dashboard implementation.

Published experience is not the same as verified mastery of every listed tool. Any future demo will contain evidence before it is labeled complete.
