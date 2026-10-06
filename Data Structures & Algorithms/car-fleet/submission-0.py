class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        fleet = 0
        max_time = 0
        for i,j in pairs:
            time = (target - i)/j
            if time>max_time:
                fleet = fleet+1
                max_time = time
        return fleet
        

        