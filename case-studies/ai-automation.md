# AI & Business Automation | Engineering Case Study

**Python · synthetic reports · optional AI review · email previews**

[Implementation](../engineering-labs/ai-business-automation/main.py) · [Tests](../engineering-labs/ai-business-automation/tests/test_main.py) · [Run instructions](../engineering-labs/ai-business-automation/README.md)

## Problem and architecture

How can an automated business reporting process generate useful outputs without accidental email delivery or disclosure of customer data?

~~~mermaid
flowchart TD
  A[Deterministic fictional records] --> B{Validate categories and unique IDs}
  B -->|Invalid| X[Fail closed]
  B -->|Valid| C[Aggregate revenue by month/channel]
  C --> D[JSON and accessible HTML]
  C --> E[UNSENT email preview]
  C --> F{Provider approved AND network allowed?}
  F -->|No| G[Local audit only]
  F -->|Yes| H[Optional API call with synthetic aggregates]
  H --> I[Save untrusted narrative draft]
  I --> G
~~~

## Original demonstration

~~~bash
python3 -m unittest discover -s engineering-labs/ai-business-automation/tests -v
python3 engineering-labs/ai-business-automation/main.py --output output/ai-demo
~~~

The generator creates 36 deterministic fictional records. The offline process produces JSON and HTML reports, an unsent EML preview and a workflow audit record.

## Verification and limitations

| Feature | Evidence |
|---|---|
| Deterministic generator and aggregate reconciliation | Python offline unit tests |
| Duplicate ID and invalid-category rejection | Test cases and implementation |
| Unsent mail preview and escaped HTML | Implementation and tests |
| No provider network calls without approval | Mocked-network tests |
| OpenAI / Anthropic optional adapters | Written source only; live provider integration unverified |
| Sending real email | Not implemented |
| Production scheduling | Not implemented |

The provider path requires explicit network/approval flags and environment-provided tokens, sends only fictitious aggregates, and never auto-emails the model output.

**Engineering lessons:** fail closed, separate calculations from narrative, control external effects, and label generated text as untrusted.

[CI evidence](https://github.com/Dicureck/Dicureck/actions/workflows/engineering-labs.yml) · [Automation methodology](../knowledge-base/ai-automation.md) · [← Case studies](README.md)
