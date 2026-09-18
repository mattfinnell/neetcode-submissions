from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            characters = "".join(sorted(s))
            table[characters].append(s)

        return list(table.values())


