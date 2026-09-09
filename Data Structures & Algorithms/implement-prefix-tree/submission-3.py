class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        current = self.root

        for v in word:
            if v not in current.children:
                current.children[v] = TreeNode()
            current = current.children[v]

        current.isEndOfWord = True


    def search(self, word: str) -> bool:
        current = self.root

        for v in word:
            if v not in current.children:
                return False
            current = current.children[v]
            if current.isEndOfWord == True:
                return True

        return False        
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for v in prefix:
            if v not in current.children:
                return False
            current = current.children[v]

        return True  
        
        