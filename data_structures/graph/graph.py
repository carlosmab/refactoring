from typing import Any, List

class Vertex:
    value: Any
    edges: List['Edge']
    
    def __init__(self, value: Any) -> None:
        self.value = value
        self.edges = []
        
    def add_edge(self, edge: 'Edge') -> None:
        self.edges.append(edge)
        
    def __str__(self):
        return self.value


class Edge:
    start: Vertex
    end: Vertex
    weight: int
    
    def __init__(self, start: Vertex, end: Vertex, weight: int = 1) -> None:
        self.start = start
        self.end = end
        self.weight = weight
        start.add_edge(self)
        end.add_edge(self)
        
    def __str__(self) -> str:
        return f'{self.start} -({self.weight})-> {self.end}'

    
class Graph:
    vertices: List[Vertex]
    
    def __init__(self) -> None:
        self.vertices: List[Vertex] = []
        
    def add_vertex(self, value: Any) -> Vertex:
        vertex = Vertex(value)
        self.vertices.append(vertex)
        return vertex
    
    def add_edge(self, start: Vertex, end: Vertex, weight: int = 1) -> None:
        edge = Edge(start, end, weight)
    
    def __str__(self) -> str:
        return "\n".join(str(vertex) for vertex in self.vertices)
    
    def print(self):
        for vertex in self.vertices:
            for edge in vertex.edges:
                print(edge)
    

graph = Graph()

vertexA = graph.add_vertex("A")
vertexB = graph.add_vertex("B")
vertexC = graph.add_vertex("C")


graph.add_edge(vertexA, vertexC)
graph.add_edge(vertexA, vertexB)
graph.add_edge(vertexB, vertexC)

graph.print()
print(graph)
