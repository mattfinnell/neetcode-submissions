class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        skinny, fat, result = 0, len(people) - 1, 0

        while skinny <= fat:
            remaining_capacity = limit - people[fat]
            fat -= 1
            result += 1

            if skinny <= fat and remaining_capacity >= people[skinny]:
                skinny += 1

        return result