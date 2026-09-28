class Solution:
    DELIMITER = "[DELIMITER]"

    def encode(self, strs: List[str]) -> str:
        lengths = [str(len(s)) for s in strs]

        return f"{','.join(lengths)}{self.DELIMITER}{''.join(strs)}"


    def decode(self, s: str) -> List[str]:
        lengths_strings_split = s.split(self.DELIMITER)
        if len(lengths_strings_split) != 2:
            return []

        lengths, strings = lengths_strings_split
        if not lengths:
            return []

        lengths = [int(length) for length in lengths.split(',')]

        result, i = [], 0
        for length in lengths:
            result.append(strings[i:i + length])
            i += length

        return result