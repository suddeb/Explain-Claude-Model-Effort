# DEMO — "didn't TRY hard enough" (bump EFFORT)

## The prompt to give Claude Code (identical both runs)
> Rename `generate_slug` to `generate_short_code` everywhere it's used, and add
> an optional `length: int = 6` parameter so callers can request a different
> code length. Then make sure the whole test suite still passes.

## Run A — LOW effort (the miss)
Expected: renames the def in `slug.py`, updates maybe one caller, declares done,
and does NOT run `pytest`. `stats.py` (and often `cli.py`) still import/call the
old name -> `ImportError` / failing tests you catch yourself.

Show this on screen:
```
pytest -q
# ImportError: cannot import name 'generate_slug' from 'linkshortener.slug'
```

## Run B — HIGHER effort (same model, same prompt)
Expected: reads all three caller modules, updates every call site, threads the
new `length` param through, THEN runs the suite and confirms green before
handing back.

Show this on screen:
```
pytest -q
# 6 passed
```

Same brain. Same prompt. It just did the work.
