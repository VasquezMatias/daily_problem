
class BinaryTree():
    def __init__(self, node, left = None, right = None) -> None:
        self.root = node
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.root) + "\t" + str(self.left) + "\t" + str(self.right)

    
class Tree():
    def __init__(self, root, left=None, right=None) -> None:
        self.tree = BinaryTree(root, left, right)

    def boustrophedon_util(self, tree, lvls, lvl):
        if lvl not in lvls:
            lvls[lvl] = []

        lvls[lvl].append(tree.root)
        
        try:
            if tree.left != None:
                lvls = self.boustrophedon_util(tree.left, lvls, lvl + 1)
        except:
            print("Left branch finished without children.")
        
        try:
            if tree.right != None:
                lvls = self.boustrophedon_util(tree.right, lvls, lvl + 1)
        except:
            print("Right branch finished without children.")

        return lvls

    def boustrophedon(self):
        lvls = {}
        lvls = self.boustrophedon_util(self.tree, lvls, 0)
        
        boustrophedon = []
        for i, key in enumerate(lvls):
            if i % 2 == 1:
                lvls[key].reverse()
            
            boustrophedon.extend(lvls[key])
        return boustrophedon

    def __repr__(self) -> str:
        return str(self.tree)


left = BinaryTree(2, BinaryTree(4), BinaryTree(5))
right = BinaryTree(3, BinaryTree(6), BinaryTree(7))
tree = Tree(1, left, right)


print(tree)
print(tree.boustrophedon())