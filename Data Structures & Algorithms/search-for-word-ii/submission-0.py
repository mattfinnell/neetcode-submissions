class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        for word in words:
            self._add_word(word)

    def _add_word(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n, visited = len(board), len(board[0]), set()
        results, visited, trie = set(), set(), Trie(words)

        for i in range(m):
            for j in range(n):
                self.find(board, i, j, results, "", trie.root, visited)

        return list(results)

    def find(self, board, i, j, results, word, trie, visited):
        m, n = len(board), len(board[0])

        if (
            i < 0 or j < 0 or i >= m or j >= n
            or (i, j) in visited
            or board[i][j] not in trie.children
        ):
            return 

        visited.add((i, j))
        trie = trie.children[board[i][j]]
        word += board[i][j]

        if trie.eow:
            results.add(word)
        
        self.find(board, i - 1, j, results, word, trie, visited)
        self.find(board, i + 1, j, results, word, trie, visited)
        self.find(board, i, j - 1, results, word, trie, visited)
        self.find(board, i, j + 1, results, word, trie, visited)

        visited.remove((i, j))