class TrieNode:
    # TrieNode class


    def __init__(self):
        self.children = [None for _ in range(26)]
        self.endofstring = False


class Trie:

    def __init__(self):

        self.root = TrieNode()


newTrie = Trie()