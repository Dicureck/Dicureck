# Security Policy

Thank you for helping maintain safe, original public engineering demonstrations.

## Project scope

This repository contains a professional GitHub profile, public technical documentation, original synthetic-data engineering labs and source-controlled Wiki tutorials.

The code and examples are **not deployed client systems**, payment processors or production databases. Public demos do not require access to private accounts, customer records or actual organizational credentials.

## Report security issues responsibly

If you find a vulnerability, accidental exposure, unsafe example, or potentially malicious dependency:

1. **Do not publish exploit details or secret values in a public GitHub Issue.**
2. Contact **[info@intebi.online](mailto:info@intebi.online)** with the affected repository/file, reproduction steps using fictitious data, observed impact and a proposed safe fix if available.
3. If GitHub's **Private vulnerability reporting** is enabled for the affected repository, you may use that private reporting option instead.
4. Allow the maintainer to review the report before publishing details that could expose others.

Avoid attaching passwords, tokens, customer exports, production server information or real personal records. If a secret has been exposed, revoke/rotate it first through the appropriate owner.

## Maintainer safety practices

- Repository demonstrations rely on synthetic data and documentation.
- AI and email adapters are offline/dry-run by default; enabling a network request should require explicit approval.
- Database migrations and DML examples must not be run on shared or production environments without written authorization and recovery planning.
- Review dependency changes, relevant CI runs and license conditions before use.
- Automated Wiki updates preserve original Home and SQL Performance pages and use a restricted allowlist.

## Supported versions and response expectations

| Material | Security maintenance |
|---|---|
| Current default-branch source | Best-effort corrections and documentation updates |
| Current published v0.1.0 laboratory releases | Reproducible snapshots; fixes will normally be published in a newer version |
| Historical commits and private third-party deployments | Not actively maintained or supported |

No formal incident-response service-level agreement or guaranteed response time is offered. This page is a reporting channel and disclosure guideline, not a security certification.

## Documentation and licensing

See the [engineering publication standards](knowledge-base/portfolio-standards.md) and the [native Wiki maintenance policy](knowledge-base/wiki-maintenance.md). This security policy does **not** grant a copyright license to the profile text, original brand artwork, images or source code; licensing choices are handled separately.

*Melissa Castro · Independent, synthetic engineering portfolio*
