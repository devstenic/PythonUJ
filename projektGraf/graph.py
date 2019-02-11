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
        self.matrix = [[0 for i in range(self.n) ] for j in range(self.n)]

    def __repr__(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix]))

    def v(self):
        """Zwraca liczbę wierzchołków"""
        return self.n


    def __eq__(self, other):
        return self.n == other.n and self.matrix == other.matrix

    def e(self):
        """Zwraca liczbę krawędzi"""
        counter = 0
        for row in self.matrix:
            for j in row:
                if j == 0:
                    continue
                elif j != 0:
                    counter += 1
        return counter if self.is_directed() else int(counter/2)


    def is_directed(self):              #
        """Bool, czy graf skierowany"""
        return self.directed

    def add_node(self, node):
        """Dodaje wierzchołek"""
        return True if 0 <= node < self.n else False

    def has_node(self, node):
        """Sprawdza czy wierzcholek istnieje, Bool"""
        return True if 0 <= node < self.n else False

    def del_node(self, node):
        """Usuwa wierzchołek"""
        if 0 >= node > self.n:
            raise ValueError('Wierzcholek nie nalezy do grafu')
        else:
            for i in range(self.v()):
                self.matrix[i][node] = 0
            for i in range(self.v()):
                self.matrix[node][i] = 0

    def add_edge(self, edge):
        """Wstawienie krawędzi"""
        source = edge.source
        target = edge.target
        weight = edge.weight
        if 0 >= (source or target) > self.n:
            raise ValueError('te wierzcholki nie naleza do grafu!')
        elif source == target:
            raise ValueError('petle nie sa obslugiwane!')
        elif not self.has_edge(Edge(source,target)) and self.is_directed():
            self.matrix[source][target] = weight
        elif not self.has_edge(Edge(source, target)):
            self.matrix[source][target] = weight
            self.matrix[target][source] = weight

    def has_edge(self, edge):
        """Sprawdza czy krawedz istnieje, Bool"""
        source = edge.source
        target = edge.target
        if 0 > (source or target) > self.n:
            raise IndexError('brak takich wierzchołkow!')
        else:
            return True if self.matrix[source][target] != 0 else False

    def del_edge(self, edge):
        """Usunięcie krawędzi"""
        source = edge.source
        target = edge.target
        if 0 <= (source or target) < self.n:
            if self.directed:
                self.matrix[source][target] = 0
                return True
            elif not self.directed:
                self.matrix[source][target] = 0
                self.matrix[target][source] = 0
                return True
        else:
            raise ValueError('te wierzcholki nie naleza do grafu!')

    def weight(self, Edge):
        """Zwraca wagę krawędzi"""
        source = Edge.source
        target = Edge.target
        if 0 >= (source or target) > self.n:
            raise IndexError('te wierzcholki nie naleza do grafu!')
        elif self.matrix[source][target] == 0:
            print('Ta krawedz nie istnieje w grafie!')
        else:
            return self.matrix[source][target]

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
        """Iterator po wierzchołkach"""
        return iter(range(self.n))

    def iteradjacent(self, node):
        """ iterator po wierzchołkach sąsiednich"""
        for item in self.matrix[node]:
            if item != 0:
                yield self.matrix[node].index(item)

    def iteroutedges(self, node):
        """Iterator po krawędziach wychodzących"""
        for item in self.matrix[node]:
            if item != 0:
                yield Edge(node, self.matrix[node].index(item), self.matrix[node][self.matrix[node].index(item)])


    def iterinedges(self, node):
        """Iterator po krawędziach przychodzących"""
        for i in range(self.v()):
            if self.has_edge(Edge(i, node)):
                yield Edge(i, node, self.matrix[i][node])


    def iteredges(self):
        """Iterator po krawędziach"""
        for i in range(self.v()):
            for j in range(self.v()):
                if self.matrix[i][j] != 0:
                    yield Edge(i, j, self.matrix[i][j])


    def iter_bfs(self, start_node):
        return BFS(self, start_node)

    def iter_dfs(self, start_node):
        return DFS(self, start_node)

    def traverse_dfs(self, start, visit=visit, visited=None):
        traverse_dfs(self, start, visit, visited=visited)

    def traverse_bfs(self, start, visit=visit):
        traverse_bfs(self, start, visit)


    def copy(self):
        """Zwraca kopię grafu"""
        newGraph = Graph(self.n, self.directed)
        newGraph.matrix = copy(self.matrix)
        return newGraph

    def transpose(self):
        """Zwraca graf transponowany"""
        newGraph = self.copy()
        newGraph.matrix = map(list, zip(*self.matrix))
        return newGraph

    def complement(self):
        """Zwraca dopełnienie grafu"""
        newGraph = self.copy()
        for row in range(self.v()):
            for col in range(self.v()):
                if newGraph.matrix[row][col] == 0:
                    newGraph.matrix[row][col] = 1
                elif newGraph.matrix[row][col] != 0:
                    newGraph.matrix[row][col] = 0
        return newGraph

    def subgraph(self, nodes):
        """Zwraca podgraf indukowany"""
        newGraph = self.copy()
        for i in nodes:
            newGraph.del_node(i)
        return newGraph


