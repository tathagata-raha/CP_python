class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class DiameterOfABinaryTree:
    def __init__(self):
        self.diameter = 0
    def height(self,node):
        if node is None:
            return 0
        lh = self.height(node.left)
        rh = self.height(node.right)
        tmp = lh + rh
        if self.diameter < tmp:
            self.diameter= tmp
        return 1 + max(lh,rh)
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height(root)
        return self.diameter
        
class BuildFromInorderAndPostorder:
    def build(self,sin, ein, spost, epost):
        
        if ein==sin:
            return None
        root = TreeNode(self.postorder[epost-1])
        if ein-sin == 1:
            return root
        idx = self.val_idx[root.val]
        # print(sin, ein, spost, epost, idx)
        root.left = self.build(sin,idx,spost, spost+(idx-sin))
        root.right = self.build(idx+1, ein, spost+(idx-sin), epost-1)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # print(inorder, postorder)
        self.inorder = inorder
        self.postorder = postorder
        self.val_idx = {v:i for i,v in enumerate(inorder)}
        root = self.build(0,len(postorder),0,len(postorder))
        return root


class Solution:
    def build(self,sin, ein, spost, epost):
        
        if ein==sin:
            return None
        root = TreeNode(self.postorder[epost-1])
        if ein-sin == 1:
            return root
        idx = self.val_idx[root.val]
        # print(sin, ein, spost, epost, idx)
        root.left = self.build(sin,idx,spost, spost+(idx-sin))
        root.right = self.build(idx+1, ein, spost+(idx-sin), epost-1)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # print(inorder, postorder)
        self.inorder = inorder
        self.postorder = postorder
        self.val_idx = {v:i for i,v in enumerate(inorder)}
        root = self.build(0,len(postorder),0,len(postorder))
        return root
        

class TreeFunctions:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def traversal(node):
            if node:
                traversal(node.left)
                res.append(node.val)
                traversal(node.right)
                
        traversal(root)
        return res
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        st = []
        res = []
        curr = root
        while True:
            while curr is not None:
                res.append(curr.val)
                st.append(curr)
                curr = curr.left
            if len(st) == 0:
                break
            curr = st.pop().right
        return res
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        st = []
        st2 = []
        curr = root
        while True:
            while curr is not None:
                st.append([curr, 0])
                curr = curr.left
            if len(st) == 0:
                return res
            while st[-1][1] != 0:
                res.append(st.pop()[0].val)
                if len(st) == 0:
                    return res
            st[-1][1] = 1
            curr = st[-1][0].right
            
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        if root is None:
            return []
        res = []
        q.append((root,0))
        while len(q)!=0:
            tmp = q.popleft()
            res.append((tmp[0].val, tmp[1]))
            if tmp[0].left is not None:
                q.append((tmp[0].left, tmp[1]+1))
            if tmp[0].right is not None:
                q.append((tmp[0].right, tmp[1]+1))
        d = defaultdict(list)
        for i in res:
            d[i[1]].append(i[0])
        return [i for i in d.values()]
        
    def calculateDiameter(self, root):
        tmp = DiameterOfABinaryTree()
        return tmp.diameterOfBinaryTree(root)
        
        
    def buildfrominandpost(self, inorder: List[int], postorder: List[int]):
        tmp = BuildFromInorderAndPostorder()
        return tmp.buildTree(inorder, postorder)