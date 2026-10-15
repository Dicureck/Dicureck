# AI & Business Automation Lab

**Status:** published standalone source inside this profile repository; network and real email delivery disabled by default.

A safe, reproducible Python 3.11+ demonstration of a reporting workflow that can be used without external packages or credentials.

## Working behavior

1. Generates deterministic synthetic business transactions using a local fixed seed.
2. Validates the records, calculates a monthly channel summary, and writes machine-readable JSON.
3. Renders an accessible, escape-safe HTML report.
4. Creates an **email preview file** in the local outbox. It does **not** send any emails.
5. Optionally requests an AI-generated narrative from **OpenAI's Responses API** or **Anthropic's Messages API**, with an explicit network flag, an approval flag and provider credentials. It only sends generated fictional aggregates.
6. The GitHub Actions workflow runs these offline tests and a scheduled dry-run only; it never calls AI APIs or sends emails.

## Try it

```bash
python3 -m unittest discover -s engineering-labs/ai-business-automation/tests -v
python3 engineering-labs/ai-business-automation/main.py --output output/ai-demo
```

Files: `report.json`, `report.html`, `email-preview.eml`, `workflow-audit.json`.

### Optional provider integration — explicit opt-in

```bash
export OPENAI_API_KEY="your-key"
export OPENAI_MODEL="your-supported-model"
python3 engineering-labs/ai-business-automation/main.py --output output/ai-demo --provider openai --allow-network --approved

export ANTHROPIC_API_KEY="your-key"
export ANTHROPIC_MODEL="your-supported-model"
python3 engineering-labs/ai-business-automation/main.py --output output/ai-demo --provider anthropic --allow-network --approved
```

**Never commit secrets.** Provider configurations are read from environment variables; the code does not embed tokens. By design no SMTP implementation exists. Optional AI responses are saved as untrusted draft text for human review, not delivered automatically.

**Limitations:** The offline test suite does not exercise real provider accounts, production scheduling or network delivery. Model names and provider API compatibility must be verified using your account. This is an original portfolio lab, not an employer or customer system.

[← Portfolio Knowledge Base](../../knowledge-base/README.md) · [Responsible Automation](../../knowledge-base/ai-automation.md)
