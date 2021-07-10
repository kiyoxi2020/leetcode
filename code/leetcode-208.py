'''
leetcode 208. 实现 Trie (前缀树)

Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Trie(object):

    class Trie_node:
        def __init__(self):
            self.isValid = False
            self.kids = [None]*26

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = self.Trie_node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        n = len(word)
        root = self.data
        i = 0
        for i in range(n):
            t = ord(word[i])-97
            if not root.kids[t]: root.kids[t] = self.Trie_node()
            root = root.kids[t]
        root.isValid = True
        return


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        root = self.data
        for i in range(n):
            t = ord(word[i])-97
            if root.kids[t] == None: return False
            root = root.kids[t]
        return root.isValid


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        n = len(prefix)
        root = self.data
        for i in range(n):
            t = ord(prefix[i])-97
            if root.kids[t] == None: return False
            root = root.kids[t]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)