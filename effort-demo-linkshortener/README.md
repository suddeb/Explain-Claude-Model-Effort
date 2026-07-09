# effort-demo-linkshortener

A deliberately tiny link shortener with **one helper used in three modules**
and a passing test suite. Built to demonstrate **Claude Code effort levels**.

```
pip install pytest
pytest -q      # should show 6 passed
```

`generate_slug` lives in `linkshortener/slug.py` and is called from
`store.py`, `cli.py`, and `stats.py`. See DEMO.md for the exact prompt.
