

class BinaryTree():
    def __init__(self, node, left=None, right=None, parent=None, level=0) -> None:
        self.node = node
        self.left = left
        self.right = right
        self.parent = parent
        self.level = level

    def __repr__(self, n=0) -> str:
        if self.left is None or self.right is None:
            return "\n"+"\t"*n + str((self.node, self.level)) + "\n"+"\t"*(n+1) + str(self.left) + "\n"+"\t"*(n+1) + str(self.right)
        return "\n"+"\t"*n + str((self.node, self.level)) + "\n"+"\t"*(n+1) + self.left.__repr__(n+1) + "\n"+"\t"*(n+1) + self.right.__repr__(n+1)


class Tree():
    def __init__(self, S: list) -> None:
        self.tree = self.build_tree(S)

    def build_tree(self, S: list, level=0) -> BinaryTree:
        if len(S)==0:
            return None

        left = [element for element in S[1:] if element < S[0]]
        right = [element for element in S[1:] if element > S[0]]

        branch = BinaryTree(S[0], self.build_tree(left, level+1), self.build_tree(right, level+1), level=level+1)
        if type(branch.left) == BinaryTree:
            branch.left.parent = branch

        if type(branch.right) == BinaryTree:
            branch.right.parent = branch
        return branch 

        
    def find_LCA(self, node_v, node_w) -> BinaryTree:
        if node_v.level < node_w.level:
            node_v = node_v.parent
        elif node_w.level < node_v.level:
            node_w = node_w.parent
        elif node_v.level == node_w.level:
            if node_v == node_w:
                return node_v
            return self.find_LCA(node_v.parent, node_w.parent)

        return self.find_LCA(node_v, node_w)

    def __repr__(self) -> str:
        return self.tree.__repr__(0)


S = [5, 3, 2, 4, 8, 7, 9]
tree = Tree(S)
print(f"Full tree: \n{tree}")

v = tree.tree.left.left
w = tree.tree.right.right
w2 = tree.tree.right.left

print(f"LCA(v, w) \n{tree.find_LCA(v, w)}")
print(f"LCA(v, v) \n{tree.find_LCA(v, v)}")
print(f"LCA(w, w) \n{tree.find_LCA(w, w)}")
print(f"LCA(w, w2) \n{tree.find_LCA(w, w2)}")