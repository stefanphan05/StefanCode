class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        start, end = N - 1, 0
        tank = gas[start] - cost[start]
        while end < start:
            if tank < 0:
                start -= 1
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1
        
        if tank < 0: return -1
        return start
"""
Brute Force:
    for every position in gas, consider it as a starting postion
        for every next position, calculate whether its able to travel around

2 Pointers
    start at the end and move backwards to the beggining
    end at the start and move forward to the end

Greedy
"""