import time

class SeatMap:
    """
    Reserves seats for an event.

    The bug is a classic CHECK-THEN-ACT race: two threads can both read a seat
    as free before either writes, so the seat gets double-booked.

    The tiny time.sleep() is ONLY here to make the race deterministic on camera
    (it forces a context switch inside the window). The race exists without it;
    the sleep just guarantees the flaky test fails every time you record.

    A less-capable run often "fixes" this by DELETING the sleep, or by adding a
    second redundant check -- neither of which closes the race. The real fix
    needs a lock around check+act (or an atomic reservation / DB unique
    constraint for multi-process). That's the judgment a larger model brings.
    """
    def __init__(self, seat_ids):
        self._owner = {sid: None for sid in seat_ids}

    def reserve(self, seat_id: str, user: str) -> bool:
        if self._owner[seat_id] is None:      # CHECK
            time.sleep(0.001)                 # <-- race window (see docstring)
            self._owner[seat_id] = user       # ACT
            return True
        return False

    def owner_of(self, seat_id: str) -> str | None:
        return self._owner[seat_id]
