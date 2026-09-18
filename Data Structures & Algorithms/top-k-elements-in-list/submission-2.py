class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter, buckets = Counter(nums), [[] for _ in range(len(nums) + 1)]

        for key, count in counter.items():
            buckets[count].append(key)

        i, result = len(buckets) - 1, []
        while i >= 0 and len(result) <= k:
            if buckets[i]:
                result.extend(buckets[i])
            
            i -= 1

        return result[:k]