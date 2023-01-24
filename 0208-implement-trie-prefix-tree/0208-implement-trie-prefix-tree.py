class trie:
    def __init__(self):
        self.arr = [None for _ in range(26)]; self.pres = False;
        
class Trie:

    def __init__(self):
        self.root = trie();

    def insert(self, word: str) -> None:
        def asci(char):
            return ord(char) - ord('a')
        temp = self.root;
        n = len(word);
        for i in range(n):
            asc = asci(word[i])
            if temp.arr[asc]:
                temp = temp.arr[asc];
            else:
                temp.arr[asc] = trie();
                temp = temp.arr[asc];
        temp.pres = True;
        
    def search(self, word: str) -> bool:
        def asci(char):
            return ord(char) - ord('a')
        n = len(word);
        temp = self.root;
        for i in range(n):
            asc = asci(word[i]);
            if temp.arr[asc]:
                temp = temp.arr[asc];
            else: return False
        return temp.pres;
            

    def startsWith(self, prefix: str) -> bool:
        def asci(char):
            return ord(char) - ord('a')
        n = len(prefix); temp = self.root;
        for i in range(n):
            asc = asci(prefix[i])
            if not temp.arr[asc]: return False
            else: temp = temp.arr[asc]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)