class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = defaultdict(list)

        for string in strs:
            frequencies[''.join(sorted(string))].append(string)

        return frequencies.values()