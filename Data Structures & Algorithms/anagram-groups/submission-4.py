from collections import defaultdict
from pprint import pprint

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1

            table[tuple(key)].append(s)

        return list(table.values())