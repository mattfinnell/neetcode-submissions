class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = ""
        for i, character in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != character:
                    return result

            result += character

        return result