class TrieNode:

    def __init__(self):
        self.children ={}
        self.endofstring = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insertstring(self,word):
        current = self.root

        for i in word:
            ch = i
            node = current.children.get(ch)

            if node == None:
                node = TrieNode()
                current.children.update({ch:node})

            current = node

        current.endofstring = True
        print("sucessfuly inserted")


newTrie = Trie()
newTrie.insertstring("App")