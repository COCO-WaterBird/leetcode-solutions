from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            cur = cur.children[ch]

        cur.is_word = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)

    def dfs(self, word: str, index: int, node: Node) -> bool:
        if node is None:
            return False

        if index == len(word):
            return node.is_word

        ch = word[index]

        if ch != ".":
            return self.dfs(word, index + 1, node.children.get(ch))

        for child in node.children.values():
            if self.dfs(word, index + 1, child):
                return True

        return False