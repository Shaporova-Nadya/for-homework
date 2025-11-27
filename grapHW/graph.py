class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = edges
    
    def __next__(self):
        if self.indx < len(self.values):
            r = self.values[self.indx]
            self.indx += 1
            return r
        raise StopIteration

    def _dfs_gen(self):
        visited = set()

        def dfs_step(vertex):
            if vertex not in visited:
                visited.add(vertex)
                yield vertex

                for edge in self.edges:
                    if edge[0] == vertex:
                        yield from dfs_step(edge[1])

                    if edge[1] == vertex:
                        yield from dfs_step(edge[0])

        for vertex in self.vertices:
            if vertex not in visited:
                yield from dfs_step(vertex)

    def __iter__(self):
        return self._dfs_gen()
        
    def dfs(self) -> None:
        for vertex in self:
            print(vertex)