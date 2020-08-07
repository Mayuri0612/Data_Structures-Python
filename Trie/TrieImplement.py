class TrieNode:
    def __init__(self):
        self.child = {}
        self.end= False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        current = self.root
        for w in word:
            if w not in current.child:
                current.child[w] = TrieNode()
            current = current.child[w]
        current.end = True


    def search(self,word):
        current = self.root
        for w in word:
            if w not in current.child:
                return False
            current = current.child[w]
        return current.end

    def startwWith(self, prefix):
        current = self.root
        for w in prefix:
            if w not in current.child:
                return False
            curr_node = current.child[w]
        return True

if __name__ == "__main__":
    
    ls = list(map(str,input().split(" ")))
    t = Trie()
    for i in ls:
        t.insert(i)
    print(ls)
    print(t.search("aat"))
    print(t.search("bat"))
    print(t.search("rat"))
    print(t.startwWith("a"))
    

