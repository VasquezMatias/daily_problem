class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Node, s: str = ""):
	if(root == None):
		s += '#'
		return s
	return f"{root.val} {serialize(root.left)} {serialize(root.right)}"

def deserialize(tree: str):
	return _deserialize(tree.split())

def _deserialize(tree: list):
	if len(tree) == 0:
		return None;

	val = tree.pop(0)
	if val == "#":
		return None

	left = _deserialize(tree);
	right = _deserialize(tree)

	return Node(val, left, right)


if __name__ == '__main__':
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	assert deserialize(serialize(node)).left.left.val == 'left.left'
