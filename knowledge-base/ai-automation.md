# Responsible AI & Business Process Automation

**Focus:** secure workflow design · email/report automation · AI-assisted development · human approval

**Status:** independent design patterns and reference prompts. There is no claim that a production ChatGPT/Claude connector, unattended email bot or enterprise integration has been shipped.

## 01 · Architecture for a fictional report workflow

~~~text
Synthetic data source
        |
        v
Schema validation --> Fail closed on invalid data
        |
        v
Generate draft report + source references
        |
        v
Optional AI review of approved, non-sensitive text
        |
        v
Human approval gate
        |
        v
Dry-run preview / local output
        |
        v
Optional explicitly authorized delivery adapter
        |
        v
Audit trail (no secrets or sensitive payloads)
~~~

## 02 · Security-by-design requirements

- Dry-run mode is the default. Never send an email just because a script was run.
- Use test mailboxes and synthetic records; do not connect to real organizational data for portfolio demos.
- Store API keys in environment variables/secret managers, never in code or generated screenshots.
- Require explicit approval before external effects such as email delivery or publishing.
- Validate recipient allowlists and use idempotency keys to prevent duplicate sends.
- Apply timeouts, rate limits and careful retry logic.
- Keep privacy-safe audit metadata without exposing email body, tokens or client identities.
- Treat AI-generated output as untrusted: validate data, URLs, commands and citations.

## 03 · Prompt design: controlled SQL review

~~~text
Role: technical reviewer.
Input: original, synthetic SQL example and declared schema.
Task: list possible correctness and performance risks.
Do not claim speedup or functional equivalence without test evidence.
Output:
1) potential issue,
2) assumptions,
3) suggested experiment,
4) required verification.
Do not emit executable production migration scripts.
~~~

The prompt is an example of structured instructions for human-supervised analysis; it is not a claim about model-specific safety guarantees.

## 04 · AI-assisted websites

Use coding assistants for scaffolding and ideas, then independently review:
- accessibility and responsive layout;
- form validation and safe DOM updates;
- dependency and license provenance;
- keyboard navigation and reduced-motion support;
- security headers, secrets and network requests;
- analytics consent and privacy disclosures if tracking is added.

A visually convincing mockup is not proof of a functional site.

## 05 · Public automation lab roadmap

1. Synthetic invoice/report generator, independently testable.
2. Mock email adapter that writes previews to disk only.
3. Approval-state model with human-confirmed transitions.
4. Optional provider adapter behind an explicit opt-in flag.
5. CI tests for failures, retries, duplicate suppression and safe logging.

**Companion:** [Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit) · [C#/.NET](csharp-dotnet.md) · [Reporting Platforms](reporting-platforms.md).

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*
