class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        slowest_time_ahead = 0
        
        for p, s in cars:
            # Calculate the time it takes for this specific car to reach the target
            time = (target - p) / s
            
            # If this car takes strictly longer than the slowest car ahead of it,
            # it cannot catch up. It forms a brand new fleet.
            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time  # This car is now the bottleneck for cars behind it
                
        return fleets