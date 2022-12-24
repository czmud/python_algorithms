class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node_runner = self.trie
        for char in word:
            if char not in node_runner:
                node_runner[char] = {}
            node_runner = node_runner[char]
        node_runner["_"] = True

    def search(self, word: str) -> bool:
        root = self.trie

        return searchRecursive( word, root)

def searchRecursive(word, root):
    if not word:
        return True if "_" in root else False
    
    next_char = word[0]

    if next_char == ".":
        for key in root.keys():
            if key == "_":
                continue
            if searchRecursive(word[1:], root[key]):
                return True
        return False
        
    if next_char not in root:
        return False
    
    return searchRecursive( word[1:], root[next_char] )