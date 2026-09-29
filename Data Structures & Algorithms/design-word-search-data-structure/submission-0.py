from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c in current.children:
                current = current.children[c]

            else:
                current.children[c] = TrieNode()
                current = current.children[c]

        current.end_of_word = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word: str, root) -> bool:
        current = root

        for i, c in enumerate(word):
            if c == ".":
                for nxt in current.children.values():
                    if self._search(word[i + 1:], nxt):
                        return True

                return False

            else:
                if c not in current.children:
                    return False
    
                current = current.children[c]

        return current.end_of_word