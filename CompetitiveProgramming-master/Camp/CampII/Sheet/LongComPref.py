class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self,str):
        cur = self.root
        for i in str:
            if i not in cur.children:
                cur.children[i] = TrieNode()

            cur = cur.children[i]

        cur.is_end = True

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strTrie = Trie()
        strs.sort()
        for string in strs:
            strTrie.addWord(string)
        
        common = ''
        cur = strTrie.root

        for letter in strs[0]:
            if len(cur.children) > 1:
                return common

            if letter in cur.children:
                common += letter

            cur = cur.children[letter]

        return common
