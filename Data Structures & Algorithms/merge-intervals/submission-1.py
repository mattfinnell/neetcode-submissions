import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max(interval[0] for interval in intervals)

        mp = [0] * (max_start + 1)
        for a, b in intervals:
            mp[a] = max(b + 1, mp[a])

        result, have, start = [], -1, -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if start == -1:
                    start = i

                have = max(mp[i] - 1, have)

            if have == i:
                result.append([start, have])
                have, start = -1, -1

        if start != -1:
            result.append([start, have])

        return result
                
