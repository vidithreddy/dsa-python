from collections import defaultdict

class Graph:
    """A simple directed graph using adjacency lists with BFS and DFS."""

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v."""
        self.graph[u].append(v)

    def _dfs_util(self, v, visited):
        """Utility function for DFS traversal."""
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)

    def dfs(self, start):
        """Perform DFS traversal starting from a given vertex."""
        visited = set()
        print("DFS traversal starting from vertex {}:".format(start))
        self._dfs_util(start, visited)
        print()

    def bfs(self, start):
        """Perform BFS traversal starting from a given vertex."""
        visited = set()
        queue = [start]
        visited.add(start)

        print("BFS traversal starting from vertex {}:".format(start))
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        print()


if __name__ == '__main__':
    # Example usage
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.bfs(2)
    g.dfs(2)