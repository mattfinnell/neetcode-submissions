from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList) 
        if endWord not in words or beginWord == endWord:
            return 0

        queue_begin, queue_end = deque([beginWord]), deque([beginWord])
        visited_begin, visited_end = {beginWord: 1}, {endWord: 1}

        while queue_begin and queue_end:
            if len(queue_begin) < len(queue_end):
                queue_begin, queue_end = queue_end, queue_begin

            for _ in range(len(queue_begin)):
                word = queue_begin.popleft()
                steps = visited_begin[word]

                for i in range(len(word)):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue

                        neighbor = word[:i] + chr(c) + word[i + 1:]
                        if neighbor not in words:
                            continue

                        if neighbor in visited_end:
                            return steps + visited_end[neighbor]
                        
                        if neighbor not in visited_begin:
                            visited_begin[neighbor] = steps + 1
                            queue_begin.append(neighbor)

        return 0

    def lexDistance(self, str1, str2):
        return sum(0 if a == b else 1 for a, b in zip(str1, str2))
