from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue, visited, words = deque([(beginWord, 1)]), set([beginWord]), set(wordList)

        if endWord not in words:
            return 0

        while queue:
            current, i = queue.popleft()

            if current == endWord:
                return i

            for nxt in wordList:
                if nxt not in visited and self.lexDistance(current, nxt) == 1:
                    visited.add(nxt)
                    queue.append((nxt, i + 1))

        return 0

    def lexDistance(self, str1, str2):
        return sum(0 if a == b else 1 for a, b in zip(str1, str2))
