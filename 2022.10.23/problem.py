

class BinaryTree():
    def __init__(self, node, left=None, right=None) -> None:
        self.node = node
        self.left = left
        self.right = right

    def __repr__(self, n) -> str:
        if self.left is None or self.right is None:
            return "\n"+"\t"*n + str(self.node) + "\n"+"\t"*(n+1) + str(self.left) + "\n"+"\t"*(n+1) + str(self.right)
        return "\n"+"\t"*n + str(self.node) + "\n"+"\t"*(n+1) + self.left.__repr__(n+1) + "\n"+"\t"*(n+1) + self.right.__repr__(n+1)

class BuildTree():
    def __init__(self, target) -> None:
        self.k = target
        self.tree = None
        self.subset = None
        self.has_subset = False

    def build_tree_util(self, S, n=0, left=True, node=0, path=[]):
        if len(S)==n:
            return None
        
        if not left:
            path.append(S[n])
            node = node + S[n] 
        
        if node==self.k:
            self.has_subset = True
            self.subset = path

        return BinaryTree(
            (path.copy(), node), 
            self.build_tree_util(S, n+1, True, node, path.copy()), 
            self.build_tree_util(S, n+1, False, node, path.copy())
        )

    def build_tree(self, S):
        if len(S)==0:
            return None
        tmp = [0]
        tmp.extend(S)
        S = tmp

        self.tree = self.build_tree_util(S)
        return self.tree

    def __repr__(self) -> str:
        return self.tree.__repr__(0)        

S = [12, 1, 61, 5, 9, 2]
k = 24

tree = BuildTree(k)
tree.build_tree(S)
print(tree.has_subset, tree.subset)