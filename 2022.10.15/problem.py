
class BinaryTree():
    def __init__(self, data) -> None:
        self.node = data
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "-" * 2 * level+repr(self.node)+"\n"
        if self.left is not None:
            ret += self.left.__str__(level+1)
        else:
            ret += "-" * 2 * (level+1)+"#\n"
        if self.right is not None:
            ret += self.right.__str__(level+1)
        else:
            ret += "-" * 2 * (level+1)+"#\n"
        return ret

    def __repr__(self) -> str:
        return str(self.node) #+ "\nl\t" + str(self.left) + "\nr\t" + str(self.right)

class Tree():
    def reconstruct_pos_order(self, l) -> BinaryTree:
        if len(l) == 0:
            return None

        last = l.pop()
        
        tree = BinaryTree(last)

        left = [i for i in l if i < last]
        right = [i for i in l if i > last]

        tree.left = self.reconstruct_pos_order(left)
        tree.right = self.reconstruct_pos_order(right)

        return tree


l = [2, 4, 3, 8, 7, 5]
tree = Tree()
print(tree.reconstruct_pos_order(l))
