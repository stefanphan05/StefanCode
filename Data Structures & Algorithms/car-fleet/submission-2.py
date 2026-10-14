class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time_to_reach_target(dist_fr_target: int, speed: int):
            return dist_fr_target / float(speed)
        
        n = len(position)
        pos_speed_time = []
        for i in range(n):
            time = time_to_reach_target(target - position[i], speed[i])
            pos_speed_time.append([position[i], speed[i], time])
        pos_speed_time.sort(key = lambda x: x[0], reverse = True)     # nlogn

        stack = []
        for i in range(n):
            _, _, curr = pos_speed_time[i]
            if i == 0:
               stack.append(curr)
               continue

            prev = stack[-1]
            if curr <= prev:
                continue
            else:
                stack.append(curr) 

        return len(stack)