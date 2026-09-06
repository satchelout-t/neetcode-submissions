class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(speed)
        cars=[]
        for i in range(n):
            time = (target - position[i]) / speed[i]
            cars.append((position[i],time))
        cars=sorted(cars,reverse=True)

        fleet=0
        lead_time=0
        for car in cars:
            if car[1] > lead_time:
                fleet+=1
                lead_time=car[1]
        return fleet