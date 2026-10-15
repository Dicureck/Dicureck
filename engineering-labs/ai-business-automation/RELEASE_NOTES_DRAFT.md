# AI & Business Automation Lab · v0.1.0 Source Release Draft

**Status:** proposed technical-preview source version. This folder is not a standalone GitHub repository or native GitHub Release.

## Published implementation

- Deterministic fictional sales data and grouped reporting.
- JSON/HTML outputs, an **unsent** EML preview and audit metadata.
- Strict checks for duplicate IDs, valid period keys, nonnegative integer amounts and allowed categories.
- Explicit approval/network flags and environment variables for optional OpenAI/Anthropic API requests.
- Unit tests that mock provider responses and ensure no unintended network access or HTML injection.

## Verification

[Engineering Labs CI](https://github.com/Dicureck/Dicureck/actions/workflows/engineering-labs.yml) verifies Python tests and offline report generation. Live provider accounts, actual email delivery and production scheduling are not covered.

## Next before a native release

- [ ] Decide whether to extract this project into a standalone repository.
- [ ] Run clean installation and test commands on a pinned commit.
- [ ] Create an authorized version tag and actual native GitHub Release.
- [ ] Attach original fictional outputs and precise known limitations.

[Documentation](README.md) · [Case study](../../case-studies/ai-automation.md)
