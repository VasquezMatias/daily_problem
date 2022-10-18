import math

class DeBrujin():
    def __init__(self):
        self.seen = set()
        self.edges = []

    def dfs(self, C: list, node: str):
        for i in range(len(C)):
            s = node + str(C[i])
            if (s not in self.seen):
                self.seen.add(s)
                self.dfs(C, s[1:])
                self.edges.append(i)

    def find(self, C: list, k: int):
        self.seen.clear()
        self.edges.clear()

        startingNode = str(C[0]) * (k - 1)
        self.dfs(C, startingNode)

        S = ""   
        # Number of edges
        l = int(math.pow(len(C), k))
        for i in range(l):
            S += str(C[self.edges[i]])
            
        S += startingNode
        return S
        

C = [0,1]
k = 3

deBrujin = DeBrujin()
print(deBrujin.find(C, k))