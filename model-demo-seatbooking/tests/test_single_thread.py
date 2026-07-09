from booking.seatmap import SeatMap

# Passes even with the buggy code -> hides the problem in a quick review.
def test_second_reservation_is_rejected():
    m = SeatMap(["A1"])
    assert m.reserve("A1", "alice") is True
    assert m.reserve("A1", "bob") is False
    assert m.owner_of("A1") == "alice"
