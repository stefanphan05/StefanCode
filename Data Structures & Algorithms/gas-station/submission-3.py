class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        if sum(gas) < sum(cost): return -1

        total = 0
        start = 0
        for i in range(N):
            diff = gas[i] - cost[i]
            total += diff
            if total < 0:
                total = 0
                start = i + 1
        
        return start

"""
Brute Force:
    for every position in gas, consider it as a starting postion
        for every next position, calculate whether its able to travel around



"""