from queue import PriorityQueue as pq
class SeatManager:

    def __init__(self, n: int):
        self.reservation = pq();
        for i in range(1, n+1): self.reservation.put(i);

    def reserve(self) -> int:
        return self.reservation.get();

    def unreserve(self, seatNumber: int) -> None:
        self.reservation.put(seatNumber);


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)