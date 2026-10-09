from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter, result = Counter(tasks), 0
        queue, heap = deque(), [-frequency for frequency in counter.values()]

        heapq.heapify(heap)

        while heap or queue:
            result += 1
            if not heap:
                time = queue[0][1]
            
            else:
                count = heapq.heappop(heap) + 1
                if count:
                    queue.append((count, result + n))

            if queue and queue[0][1] == result:
                heapq.heappush(heap, queue.popleft()[0])

        return result
