from edge import Edge
from copy import *
from bfs import BFS
from dfs import DFS
from traverse import *

class Graph:
    """Klasa dla grafu wazonego, skierowanego lub nieskierowanego."""
    def __init__(self, n, directed=False):
        if n <= 0:
            raise ValueError('podaj liczbe wieksza od zera!')
        self.n = n
        self.directed = directed        # bool, czy graf skierowany
        self.nodes = [i for i in range(self.n)]
        self.matrix = [[0 for i in range(self.n) ] for j in range(self.n)]

    def __repr__(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix]))

    def v(self):
        return len(self.nodes)
        # zwraca liczbę wierzchołków

    def __eq__(self, other):
        return self.nodes == other.nodes and self.matrix == other.matrix

    def e(self):
        counter = 0
        for row in self.matrix:
            for j in row:
                if j == 0:
                    continue
                elif j != 0:
                    counter += 1
        return counter if self.is_directed() else int(counter/2)
        # zwraca liczbę krawędzi

    def is_directed(self):              # bool, czy graf skierowany
        return self.directed

    def add_node(self, node):
        return True if node in self.nodes else False
        # dodaje wierzchołek

    def has_node(self, node):
        return True if node in self.nodes else False
        # bool

    def del_node(self, node):
        if node not in self.nodes:
            raise ValueError('Wierzcholek nie nalezy do grafu')
        else:
            for i in self.nodes:
                self.matrix[i][node] = 0
            for i in self.nodes:
                self.matrix[node][i] = 0
    # usuwa wierzchołek

    def add_edge(self, edge):
        source = edge.source
        target = edge.target
        weight = edge.weight
        if source and target not in self.nodes:
            raise ValueError('te wierzcholki nie naleza do grafu!')
        elif source == target:
            raise ValueError('petle nie sa obslugiwane!')
        elif not self.has_edge(Edge(source,target)) and self.is_directed():
            self.matrix[source][target] = weight
        elif not self.has_edge(Edge(source, target)):
            self.matrix[source][target] = weight
            self.matrix[target][source] = weight

    # wstawienie krawędzi

    def has_edge(self, edge):
        source = edge.source
        target = edge.target
        if (source or target) not in self.nodes:
            raise ValueError('brak takich wierzchołkow!')
        else:
            return True if self.matrix[source][target] != 0 else False
    # bool

    def del_edge(self, edge):
        source = edge.source
        target = edge.target
        if (source or target) in self.nodes:
            self.matrix[source][target] = 0
            return True
        else:
            raise ValueError('te wierzcholki nie naleza do grafu!')
    # usunięcie krawędzi

    def weight(self, Edge):
        source = Edge.source
        target = Edge.target
        if (source or target) not in self.nodes:
            raise ValueError('te wierzcholki nie naleza do grafu!')
        elif self.matrix[source][target] == 0:
            print('Ta krawedz nie istnieje w grafie!')
        else:
            return self.matrix[source][target]
    # zwraca wagę krawędzi

    def __iter__(self):
        return iter(range(self.n))

    def __getitem__(self, item):
        # if self.is_directed():
        #     raise ValueError("Graf jest skierowany")
        if item not in self:
            raise ValueError("Wierzcholek nie istnieje.")
        n_vertices = []
        for i in range(self.v()):
            if self.matrix[item][i] > 0:
                n_vertices.append(i)
        return n_vertices

    def iternodes(self):
        return iter(self.nodes)
    # iterator po wierzchołkach

    def iteradjacent(self, node):
        av = []
        for i in range(self.v()):
            if self.has_edge(Edge(node, i)):
                av.append(i)
        return iter(av)

    # iterator po wierzchołkach sąsiednich

    def iteroutedges(self, node):
        ae = []
        for i in range(self.v()):
            if self.has_edge(Edge(node, i)):
                ae.append(Edge(node, i, self.matrix[node][i]))
        return iter(ae)

    # iterator po krawędziach wychodzących

    def iterinedges(self, node):
        ae = []
        for i in range(self.v()):
            if self.has_edge(Edge(i, node)):
                ae.append(Edge(i, node, self.matrix[i][node]))
        return iter(ae)

    # iterator po krawędziach przychodzących

    def iteredges(self):
        ae = []
        for i in range(self.v()):
            for j in range(self.v()):
                if self.has_edge(Edge(i, j)):
                    ae.append(Edge(i, j, self.matrix[i][j]))
        return iter(ae)

    # iterator po krawędziach


    def iter_bfs(self, start_node):
        return BFS(self, start_node)

    def iter_dfs(self, start_node):
        return DFS(self, start_node)

    def traverse_dfs(self, start, visit=visit, visited=None):
        traverse_dfs(self, start, visit, visited=visited)

    def traverse_bfs(self, start, visit=visit):
        traverse_bfs(self, start, visit)


    def copy(self):
        newGraph = Graph(self.n, self.directed)
        newGraph.matrix = copy(self.matrix)
        newGraph.nodes = self.nodes
        return newGraph
    # zwraca kopię grafu

    def transpose(self):
        newGraph = self.copy()
        newGraph.matrix = map(list, zip(*self.matrix))
        return newGraph
    # zwraca graf transponowany

    def complement(self):
        newGraph = self.copy()
        for row in range(len(self.nodes)):
            for col in range(len(self.nodes)):
                if newGraph.matrix[row][col] == 0:
                    newGraph.matrix[row][col] = 1
                elif newGraph.matrix[row][col] != 0:
                    newGraph.matrix[row][col] = 0
        return newGraph
    # zwraca dopełnienie grafu

    def subgraph(self, nodes):
        newGraph = self.copy()
        for i in nodes:
            newGraph.del_node(i)
        return newGraph
    # zwraca podgraf indukowany


test = Graph(4)
test.add_edge(Edge(2,3))
test.__repr__()