# Contributing

Small PRs and bug reports are welcome. Larger refactors — open an issue first so we can agree on scope before you spend time.

## Setup

```bash
git clone https://github.com/alex-jb/claude-tier-router.git
cd claude-tier-router
pip install -e '.[dev]'
pytest
```

All 8 tests should pass in under a second. They use mocks — no Anthropic API key needed for development.

## What a good PR looks like

- One focused change, one commit (or a clean series)
- Tests for new behavior, not just the happy path
- `pytest -v` green on Python 3.9+ before pushing (CI will catch this too)
- `pyflakes src tests` clean
- README or CHANGELOG updated when behavior changes

## What we'll probably merge quickly

- **Bug fixes** with a failing test that reproduces the bug
- **New routing methods** that follow the existing `fast()` / `deep()` pattern
- **Additional model entries** in `PRICING_USD_PER_TOKEN` when Anthropic releases new models
- **Docs improvements** — examples, clearer anti-patterns, cost benchmarks

## What we'll push back on

- **Adding non-Anthropic providers** — this is explicitly a Claude-only library. If you want multi-provider, fork and build `llm-tier-router`.
- **Streaming-specific routing logic** — keep the API surface minimal. Streaming works through `**kwargs` passthrough.
- **Config frameworks, pydantic settings, hydra** — this is ~150 LOC on purpose.

## Reporting bugs

Open an issue with:
- What you ran (minimal repro)
- What you expected
- What you got
- Python version + `anthropic` SDK version

Security issues — email instead of opening a public issue.

## License

By contributing you agree your contributions are MIT licensed.
