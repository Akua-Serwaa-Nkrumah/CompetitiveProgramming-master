class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self,word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()

            cur = cur.children[w]

        cur.is_end = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        diction = Trie()

        for w in words:
            diction.addWord(w)

        row, col = len(board), len(board[0])
        ans, visited = set(), set()

        def dfs(r,c, node, word):
            if r < 0 or c < 0 or r == row or c == col or (r,c) in visited or board[r][c] not in node.children or (r,c) in visited:
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end:
                ans.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            dfs(r-1,c,node,word)

            visited.remove((r,c))

        for i in range(row):
            for j in range(col):
                dfs(i,j, diction.root,"")

        return list(ans)

           

        