# model-demo-seatbooking

A minimal in-memory seat-reservation class with a **check-then-act race
condition**. Single-threaded test passes; concurrent test fails. Built to
demonstrate **Claude Code model selection** (capability, not effort).

```
pip install pytest
pytest -q tests/test_single_thread.py   # 1 passed (looks fine!)
pytest -q tests/test_concurrent.py      # FAILS: seat double-booked
```

See DEMO.md for the exact prompt and what each model should/shouldn't catch.
