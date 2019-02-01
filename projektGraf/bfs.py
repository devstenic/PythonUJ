import queue


class BFS:
    def __init__(self, graph, node):
        self.graph = graph
        self.node = node
        self.visited = [False for i in range(graph.v())]
        self.vQueue = queue.Queue()
        self.vQueue.put(self.node)
        self.visited[self.node] = True

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vQueue.empty():
            self.node = self.vQueue.get()
            for node in self.graph[self.node]:
                if not self.visited[node]:
                    self.vQueue.put(node)
                    self.visited[node] = True
            return self.node
        else:
            raise StopIteration
