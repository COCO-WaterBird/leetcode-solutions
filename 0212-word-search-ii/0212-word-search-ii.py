class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # 1. 建 Trie
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        m = len(board)
        n = len(board[0])
        res = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            # 边界判断
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            ch = board[r][c]

            # 已访问过，或者 Trie 里没有这个字符
            if ch == "#" or ch not in node.children:
                return

            next_node = node.children[ch]

            # 找到一个完整单词
            if next_node.word is not None:
                res.append(next_node.word)

                # 防止重复加入同一个单词
                next_node.word = None

            # 标记当前格子已访问
            board[r][c] = "#"

            # 探索上下左右
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # 回溯，恢复现场
            board[r][c] = ch

        # 2. 从每个格子出发
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res        