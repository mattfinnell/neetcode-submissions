class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        s1_frequencies, window_frequencies = Counter(s1), Counter(s2[:m])

        if s1_frequencies == window_frequencies:
            return True

        for i in range(m, n):
            window_frequencies[s2[i]] += 1

            left = s2[i - m]
            window_frequencies[left] -= 1
            if not window_frequencies[left]:
                del window_frequencies[left]

            if window_frequencies == s1_frequencies:
                return True
        
        return False