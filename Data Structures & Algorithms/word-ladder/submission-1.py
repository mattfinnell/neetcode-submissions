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

            for pos in range(len(current)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = current[:pos] + c + current[pos+1:]
                    if nxt in words and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, i + 1))

        return 0
