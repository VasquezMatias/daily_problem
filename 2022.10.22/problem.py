
class Node:
    def __init__(self, dataval=None, nextval=None) -> None:
        self.dataval = dataval
        self.nextval = nextval

    def __repr__(self) -> str:
        if self.nextval is None:
            return str(self.dataval)

        return str(self.dataval) + ", " + str(self.nextval)

class SingleLinkedList:
    def __init__(self, head: Node=None) -> None:
        self.headval = head

    def remove_k_last(self, k):
        i = 0
        k = -k - 1
        item_last = self.headval
        item_k = self.headval
        
        while item_last.nextval is not None:
            i += 1
            k += 1
            item_last = item_last.nextval
            if k >= 0:
                item_k = item_k.nextval

        item_k.nextval = item_k.nextval.nextval

        return self.headval

    def __repr__(self) -> str:
        return str(self.headval)

    

d7 = Node(8)
d6 = Node(7, d7)
d5 = Node(6, d6)
d4 = Node(5, d5)
d3 = Node(4, d4)
d2 = Node(3, d3)
d1 = Node(2, d2)
d0 = Node(1, d1)

s_linked_list = SingleLinkedList(d0)

print(s_linked_list)
print(s_linked_list.remove_k_last(4))