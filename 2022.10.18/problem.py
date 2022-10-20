
class Graph():
    def __init__(self, edges) -> None:
        self.graph = dict()
        self.edges = edges
        self.build_graph(edges)
        self.V = len(self.graph)

    def build_graph(self, edges) -> None:
        self.graph.clear()
        for a, b in edges:
            if a in self.graph:
                self.graph[a].append(b)
            else:
                self.graph[a] = [b]

            if b in self.graph:
                self.graph[b].append(a)
            else:
                self.graph[b] = [a]

    def check_loop_util(self, v, key, visited, parent):
 
        # Mark the current node as visited
        visited[v] = True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for j, sub_key in enumerate(self.graph[key]):
 
            # If the node is not
            # visited then recurse on it
            if visited[j] == False:
                if(self.check_loop_util(j, sub_key, visited, v)):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != j:
                return True
 
        return False

    def check_loop(self) -> bool:
        # Mark all the vertices
        # as not visited
        visited = [False]*(self.V)
 
        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i, key in enumerate(self.graph):

            visited = [False]*(self.V)

            # Don't recur for u if it
            # is already visited
            if visited[i] == False:
                if(self.check_loop_util(i, key, visited, -1)) == True:
                    print(visited)
                    return True
 
        return False

    def __repr__(self) -> str:
        return str(self.graph)


edges = [
    ["A", "B"], ["B", "C"],
    ["C", "D"], ["D", "E"],
    ["E", "F"], ["F", "G"],
    ["G", "H"], ["H", "I"]
]

graph = Graph(edges)
print(graph.check_loop())