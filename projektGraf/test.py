from graph import Graph
from edge import Edge
import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.dGraph = Graph(15, directed=True)
        self.uGraph = Graph(15)

        self.dGraph.add_edge(Edge(0, 2))
        self.dGraph.add_edge(Edge(2, 6, 7))
        self.dGraph.add_edge(Edge(2, 7))
        self.dGraph.add_edge(Edge(7, 13))
        self.dGraph.add_edge(Edge(5, 11, 4))
        self.dGraph.add_edge(Edge(5, 12))
        self.dGraph.add_edge(Edge(0, 1))
        self.dGraph.add_edge(Edge(3, 14))
        self.dGraph.add_edge(Edge(1, 4))
        self.dGraph.add_edge(Edge(2, 5))
        self.dGraph.add_edge(Edge(1, 3))
        self.dGraph.add_edge(Edge(3, 8))
        self.dGraph.add_edge(Edge(4, 10, 11))
        self.dGraph.add_edge(Edge(4, 9))


        self.uGraph.add_edge(Edge(0, 1))
        self.uGraph.add_edge(Edge(0, 2))
        self.uGraph.add_edge(Edge(1, 3))
        self.uGraph.add_edge(Edge(2, 5))
        self.uGraph.add_edge(Edge(2, 6, 6))
        self.uGraph.add_edge(Edge(1, 4))
        self.uGraph.add_edge(Edge(2, 7))
        self.uGraph.add_edge(Edge(3, 8))
        self.uGraph.add_edge(Edge(4, 9))
        self.uGraph.add_edge(Edge(5, 11))
        self.uGraph.add_edge(Edge(4, 10, 12))
        self.uGraph.add_edge(Edge(5, 12))
        self.uGraph.add_edge(Edge(7, 13))
        self.uGraph.add_edge(Edge(3, 14))

        

    def test_init(self):
        self.assertNotEqual(self.dGraph, self.uGraph)

    def test_is_directed(self):
        self.assertTrue(self.dGraph.is_directed())
        self.assertFalse(self.uGraph.is_directed())

    def test_v(self):
        self.assertEqual(self.dGraph.v(), 15)
        self.assertEqual(self.uGraph.v(), 15)

    def test_e(self):
        self.assertEqual(self.dGraph.e(), 14)
        self.assertEqual(self.uGraph.e(), 14)

    def test_add_node(self):
        self.assertTrue(self.dGraph.add_node(6))
        self.assertTrue(self.uGraph.add_node(6))
        self.assertFalse(self.dGraph.add_node(20))
        self.assertFalse(self.uGraph.add_node(52))
        self.assertEqual(15, self.dGraph.v())

    def test_del_node(self):
        self.assertTrue(self.dGraph.has_edge(Edge(4, 10)))
        self.dGraph.del_node(4)
        self.assertFalse(self.dGraph.has_edge(Edge(4, 10)))
        self.assertTrue(self.uGraph.has_edge(Edge(4, 10)))
        self.assertTrue(self.uGraph.has_edge(Edge(10, 4)))
        self.uGraph.del_node(4)
        self.assertFalse(self.uGraph.has_edge(Edge(4, 10)))
        self.assertFalse(self.uGraph.has_edge(Edge(10, 4)))

    def test_has_node(self):
        self.assertTrue(self.dGraph.has_node(4))
        self.assertTrue(self.dGraph.has_node(8))
        self.assertFalse(self.dGraph.has_node(40))
        self.assertTrue(self.uGraph.has_node(4))
        self.assertTrue(self.uGraph.has_node(8))
        self.assertFalse(self.uGraph.has_node(40))

    def test_add_edge(self):
        self.dGraph.add_edge(Edge(3, 4, 5))
        self.assertFalse(self.dGraph.has_edge(Edge(3, 5, 5)))
        self.assertTrue(self.dGraph.has_edge(Edge(3, 4)))

        self.uGraph.add_edge(Edge(3, 4, 5))
        self.assertTrue(self.uGraph.has_edge(Edge(4, 3, 5)))
        self.assertTrue(self.uGraph.has_edge(Edge(4, 3)))

    def test_has_edge(self):
        self.assertTrue(self.dGraph.has_edge(Edge(2, 5)))
        self.assertFalse(self.dGraph.has_edge(Edge(10, 1)))
        with self.assertRaises(IndexError):
            self.dGraph.has_edge(Edge(40, 8))

    def test_del_edge(self):
        l_edges = self.dGraph.e()
        self.assertTrue(self.dGraph.has_edge(Edge(5, 12)))
        self.dGraph.del_edge(Edge(5, 12))
        self.assertFalse(self.dGraph.has_edge(Edge(5, 12)))
        self.assertEqual(l_edges - 1, self.dGraph.e())
        with self.assertRaises(ValueError):
            self.dGraph.del_edge(Edge(111, 12))

        self.assertTrue(self.uGraph.has_edge(Edge(5, 12)))
        self.assertTrue(self.uGraph.has_edge(Edge(12, 5)))
        self.uGraph.del_edge(Edge(5, 12))
        self.assertEqual(False, self.uGraph.has_edge(Edge(5, 12)))
        self.assertFalse(self.uGraph.has_edge(Edge(12, 5)))

    def test_weight(self):
        self.assertEqual(7, self.dGraph.weight(Edge(2, 6)))
        self.assertEqual(None, self.dGraph.weight(Edge(0, 6,)))
        self.assertEqual(11, self.dGraph.weight(Edge(4, 10)))
        with self.assertRaises(IndexError):
            self.dGraph.weight(Edge(1111, 6))

# Tu Ci zmieniłem :D
    def test_copy(self):
        copy_dGraph = self.dGraph.copy()
        self.assertTrue(self.dGraph == copy_dGraph)

    def test_transpose(self):
        self.dGraph.__repr__()
        self.dGraph.transpose().__repr__()
    #
    def test_iternodes(self):
        for node in self.dGraph.iternodes():
            print(node)
    #
    def test_iteradjacent(self):
        for node in self.dGraph.iteradjacent(1):
            print(node)
    #
    def test_iteroutedges(self):
        for node in self.dGraph.iteroutedges(1):
            print(node)
    #
    def test_iterinedges(self):
        for node in self.dGraph.iterinedges(1):
            print(node)

    def test_iteredges(self):
        for node in self.dGraph.iteredges():
            print(node)
    #
    def test_traverse_dfs(self):
        self.dGraph.traverse_dfs(0)

    def test_traverse_bfs(self):
        self.dGraph.traverse_bfs(0)

    def test_iter_dfs(self):
        for node in self.dGraph.iter_dfs(0):
            print(node)

    def test_iter_bfs(self):
        for node in self.dGraph.iter_bfs(0):
            print(node)


if __name__ == '__main__':
    unittest.main()


