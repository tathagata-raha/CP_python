

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                p[cur] = {}
            p = p[cur]
        p[2] = 1
    
    def search(self, num):
        if not self.root: 
            return -1
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                return False
            p = p[cur]
        return 2 in p and p[2] == 1
        
    def delete(self, num):
        if not self.root: 
            return -1
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                return False
            p = p[cur]
        p[2] = 0
        return True
    def query(self, num):
        if not self.root: 
            return -1
        p, ans = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                ans |= (1 << i)
            else:
                p = p[cur]
        return ans

tr = Trie()
tr.insert(2)
tr.insert(3)
tr.insert(4)
tr.insert(5)
tr.insert(6)
tr.insert(7)
print(tr.search(1), tr.search(3), tr.search(4))
tr.delete(3)
tr.delete(4)
print(tr.search(1), tr.search(3), tr.search(4))
