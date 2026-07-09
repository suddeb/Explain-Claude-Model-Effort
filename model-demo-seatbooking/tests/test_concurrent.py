import threading
from booking.seatmap import SeatMap

# The flaky/failing test. With the check-then-act bug, two threads both see the
# seat as free -> two Trues -> double-booked. Exactly one should ever succeed.
def test_only_one_thread_can_reserve_a_seat():
    m = SeatMap(["A1"])
    results = []
    lock = threading.Lock()

    def try_reserve(user):
        ok = m.reserve("A1", user)
        with lock:
            results.append(ok)

    threads = [threading.Thread(target=try_reserve, args=(f"user{i}",))
               for i in range(20)]
    for t in threads: t.start()
    for t in threads: t.join()

    assert results.count(True) == 1, (
        f"seat double-booked: {results.count(True)} threads won the same seat"
    )
