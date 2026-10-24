class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right

        while left <= right:
            capacity = (left + right) // 2

            if self._can_ship(weights, capacity, days):
                result = min(result, capacity)
                right = capacity - 1

            else:
                left = capacity + 1

        return result

    def _can_ship(self, weights, capacity, days):
        ships, current_capacity = 1, capacity

        for weight in weights:
            if current_capacity - weight < 0:
                ships += 1

                if ships > days:
                    return False

                current_capacity = capacity

            current_capacity -= weight

        return True
