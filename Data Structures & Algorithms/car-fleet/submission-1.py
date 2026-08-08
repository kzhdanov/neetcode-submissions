class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        f = 0
        prev_time = 0

        for pos, s in cars:
            time = (target - pos) / s

            if time > prev_time:
                prev_time = time
                f += 1

        return f        