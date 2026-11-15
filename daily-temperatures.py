class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temps = []
        
        for i in range(len(temperatures)):
            while len(temps) != 0 and temps[-1][0] < temperatures[i]:
                t = temps.pop()[1]
                temperatures[t] = i-t
            temps.append((temperatures[i], i))
        while len(temps) > 0:
            t = temps.pop()[1]
            temperatures[t] = 0
        return temperatures
                
                
        
