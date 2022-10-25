
class Graph():
    def __init__(self, edges:list) -> None:
        self.edges = edges
        self.graph = self.build_graph(edges)

    def build_graph(self, edges: list) -> dict:
        graph = dict()

        for a, b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]

        return graph

    def bipartite_util(self, node, visited:list = []):
        for element in self.graph[node]:
            if element not in visited:
                visited.append(element)
                self.bipartite_util(element, visited)
            
    def bipartite(self) -> bool:
        visited = []
        node = next(iter(self.graph))
        visited.append(node)
        self.bipartite_util(node, visited)

        print(visited)
        return len(visited) != len(self.graph)

    def __repr__(self) -> str:
        return str(self.graph) + "\t" + str(len(self.graph))



edges = [
    ["A", "B"], ["B", "C"],
    ["C", "D"], ["D", "E"],
    ["E", "F"], ["F", "G"],
    ["G", "H"], ["O", "I"]
]

graph = Graph(edges)
print(graph)
print(graph.bipartite())