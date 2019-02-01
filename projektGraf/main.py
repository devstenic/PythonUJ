from edge import Edge
from graph import Graph
from dfs import DFS
from bfs import BFS
from traverse import *
import random


dGraph = Graph(8, True)
uGraph = Graph(8)

print('Generowanie grafu: \n')

for i in range(7):
    dGraph.add_node(i)
    uGraph.add_node(i)

for i in range(random.randint(1, dGraph.v())):
    for j in range(random.randint(1, dGraph.v())):
        if i != j:
            dGraph.add_edge(Edge(i, j, random.randint(1,20)))
            uGraph.add_edge(Edge(i, j, random.randint(1,20)))

print("Reprezentacja  grafu na macierzy: \n")

dGraph.__repr__()
print('\n')
uGraph.__repr__()

print('Czy graf skierowany? ' + str(dGraph.is_directed()))
print('Czy graf skierowany? ' + str(uGraph.is_directed()))

print('\n')

print('Ilosc wierzcholkow grafu skierowanego: ' + str(dGraph.v()))
print('Ilosc wierzcholkow grafu nieskierowanego: ' + str(uGraph.v()))

print('\n')

print('Ilosc krawedzi grafu skierowanego: ' + str(dGraph.e()))
print('Ilosc krawedzi grafu nieskierowanego: ' + str(uGraph.e()))

print('\n')

print('Czy graf skierowany posiada wierzcholek 2?: ' + str(dGraph.has_node(2)))
print('Czy graf nieskierowany posiada wierzcholek 2?: ' + str(uGraph.has_node(2)))

print('\n')

print('Czy graf skierowany posiada krawedz 1 -> 2: ' + str(dGraph.has_edge(Edge(1,2))))
print('Czy graf nieskierowany posiada krawedz 2 -> 3: ' + str(uGraph.has_edge(Edge(2,3))))

print('\n')

print('Usuniecie krawedzi 1 -> 2 w grafie skierowanym jesli istnieje: ')
dGraph.del_edge(Edge(1, 2))
print('\n Reprezentacja po usunieciu: \n')
dGraph.__repr__()
print('Usuniecie krawedzi 2 - 3 w grafie nieskierowanym jesli istnieje: ')
uGraph.del_edge(Edge(2, 3))
print('\n Reprezentacja po usunieciu: \n')
uGraph.__repr__()

print('\n')

print('Usuniecie wierzchołka 4 w grafie skierowanym jesli istnieje: ')
dGraph.del_node(4)
print('\n Reprezentacja po usunieciu: \n')
dGraph.__repr__()
print('Usuniecie wierzcholka 4 w grafie nieskierowanym jesli istnieje: ')
uGraph.del_node(4)
print('\n Reprezentacja po usunieciu: \n')
uGraph.__repr__()

print('\n')

print('Waga krawedzi 1 -> 2 w grafie skierowanym jesli istnieje: ')
dGraph.weight(Edge(1, 2))
print('\n Reprezentacja po usunieciu: \n')
dGraph.__repr__()
print('Waga krawedzi 2 - 3 w grafie nieskierowanym jesli istnieje: ')
uGraph.weight(Edge(2, 3))
print('\n Reprezentacja po usunieciu: \n')
uGraph.__repr__()

print('Podgraf grafu skierowanego po zredukowaniu wierzcholkow 3 i 4: ')
print('\n Reprezentacja po operacji: \n')
dGraph.subgraph([3,4]).__repr__()
print('Podgraf grafu nieskierowanego po zredukowaniu wierzcholkow 3 i 4: ')
print('\n Reprezentacja po operacji: \n')
uGraph.subgraph([3,4]).__repr__()

print('\n')


print('Dopelnienie grafu skierowanego: ')
print('\n Reprezentacja po operacji: \n')
dGraph.complement().__repr__()
print('Dopelnienie grafu nieskierowanego: ')
print('\n Reprezentacja po operacji: \n')
uGraph.complement().__repr__()


print('\n')


print('Transpozycja grafu skierowanego: ')
print('\n Reprezentacja po operacji: \n')
dGraph.transpose().__repr__()
print('Transpozycja grafu nieskierowanego: ')
print('\n Reprezentacja po operacji: \n')
uGraph.transpose().__repr__()



print("Iterator po wierzcholkach sasiednich")
for i in dGraph.iteradjacent(2):
    print(i)

print("Iterator po krawedziach wychodzacych")
for i in dGraph.iteroutedges(2):
    print(i)

print("Iterator po krawedziach przychodzacych")
for i in dGraph.iterinedges(2):
    print(i)

print("Iterator po krawedziach")
for i in dGraph.iteredges():
    print(i)


print('BFS \n')
bfs = BFS(dGraph, 2)
iter_bfs = iter(bfs)
for i in iter_bfs:
    print(i)

for i in dGraph.iter_bfs(2):
    print(i)

print("DFS \n")
dfs = DFS(dGraph, 2)
iter_dfs = iter(dfs)
for i in iter_dfs:
    print(i)

for i in dGraph.iter_dfs(2):
    print(i)

for node in dGraph:  # iterator po wierzchołkach
    print("wierzchołek", node)

for node in uGraph:  # iterator po wierzchołkach
    print("wierzchołek ", node)
    print("stopien ", len(uGraph[node]))

uGraph.__repr__()

for target in uGraph[1]:  # iterator po sąsiadach
    print ("data 1", "sąsiaduje z", target)

print(1 in uGraph[2])  # bool, czy jest sąsiadem

for source in dGraph:  # iteracja po krawędziach bez wag
    for target in dGraph[source]:
        print("krawędź", (source, target))


print([node for node in dGraph if not dGraph[node]])
# lista wierzcholkow izolowanych

print(sorted(len(uGraph[node]) for node in uGraph))
# posortowana lista stopni wierzcholkow grafu nieskierowanego

dGraph.traverse_dfs(2)
for i in dGraph.iter_dfs(2):
    print(i)

dGraph.traverse_bfs(2)
for i in dGraph.iter_bfs(2):
    print(i)

dGraph.__repr__()
