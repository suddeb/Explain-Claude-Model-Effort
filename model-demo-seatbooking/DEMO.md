# DEMO — "didn't KNOW enough" (change MODEL)

## Why this is a MODEL demo, not an EFFORT demo
All the context is already in front of Claude: both tests, the failing output,
the class. Cranking effort doesn't help -- the problem needs the *recognition*
that this is a check-then-act race and the *judgment* to pick the right fix.
That recognition lives in more capable weights.

## The prompt to give Claude Code (identical both runs)
> `test_concurrent.py` fails intermittently — two users end up owning seat A1.
> Find the root cause and fix `reserve` so a seat can never be double-booked.
> Explain the trade-offs of your fix.

## Run A — smaller model (confidently wrong)
Watch for the common wrong turns:
- deletes the `time.sleep(...)` and claims the race is gone (it isn't)
- adds a second `if self._owner[seat_id] is None` check (still racy)
- says "looks thread-safe to me" and moves on

## Run B — larger model (the judgment)
Expected: names it as a check-then-act race, wraps check+act in a
`threading.Lock` (or uses an atomic reservation), tests go green, AND it
volunteers the trade-off you didn't ask for -- e.g. an in-process lock only
protects a single process; across processes/pods you'd want a DB unique
constraint or optimistic concurrency. That unprompted architectural nuance is
the whole point of the beat.

Green run to show on screen:
```
pytest -q            # 2 passed
```
