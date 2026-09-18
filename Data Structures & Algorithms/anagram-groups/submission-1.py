from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for word in strs:
            table[''.join(sorted(word))].append(word)
        
        return list(table.values())