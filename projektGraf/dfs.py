class DFS:
    def __init__(self, graph, node):
        self.graph = graph
        self.node = node
        self.visited = []
        self.vStack = [node]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.vStack) > 0:
            self.node = self.vStack.pop()
            if self.node not in self.visited:
                self.visited.append(self.node)
                for node in self.graph[self.node]:
                    if node not in self.visited:
                        if node not in self.vStack:
                            self.vStack.append(node)
            return self.node
        else:
            raise StopIteration
