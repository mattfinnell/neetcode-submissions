from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in graph}

        for word_a, word_b in zip(words[:-1], words[1:]):
            min_length = min(len(word_a), len(word_b))

            # circuit break: cannot make a comparison
            if len(word_a) > len(word_b) and word_a[:min_length] == word_b[:min_length]:
                return ""

            for i in range(min_length):
                a, b = word_a[i], word_b[i]
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1

                    # early break: don't need to compare the rest of the strings
                    break

        # bfs queue initialized to all indegree == 0, since those are start points
        queue, result = deque([c for c in indegree if indegree[c] == 0]), []

        while queue:
            character = queue.popleft()
            result.append(character)

            for neighbor in graph[character]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(indegree):
            return ""

        return "".join(result)
        