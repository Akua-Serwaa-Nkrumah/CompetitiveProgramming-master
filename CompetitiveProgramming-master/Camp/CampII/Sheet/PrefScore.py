from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.cnt = 0        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.memo = defaultdict(int)

    def addWord(self,string):
        cur = self.root

        mem = ''
        for s in string:
            mem += s
            if s not in cur.children:
                cur.children[s] = TrieNode()

            cur = cur.children[s]
            cur.cnt += 1

        cur.is_end = True

    def searchScore(self,string):
        cur = self.root
        ans = 0

        for s in string:
            cur = cur.children[s]
            ans += cur.cnt

        return ans

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        wordTrie = Trie()

        for word in words:
            wordTrie.addWord(word)

        score = [0]*len(words)
    
        for i in range(len(words)):
            score[i] = wordTrie.searchScore(words[i])

        return score