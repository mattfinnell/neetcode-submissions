from collections import defaultdict
from pprint import pprint

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            key = str(sorted(s))
            table[key].append(s)


        return list(table.values())