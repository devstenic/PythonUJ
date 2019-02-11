import queue


def visit(node):
    """Pewna operacja na wierzchołku"""
    print('odwiedzamy', node)


def traverse_dfs(graph, start, visit, visited=None):
    # Przy pierwszym wywołaniu funkcji traverse_dfs
    # tworzymy pustą listę węzłów odwiedzonych.
    if visited is None:
        visited = []
    # Odwiedzamy wszystkie węzły dołączone do węzła start.
    visit(start)
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            traverse_dfs(graph, node, visit, visited)


def traverse_bfs(graph, start, visit):
    q = queue.Queue()
    visited = []
    q.put(start)
    while not q.empty():
        start = q.get()
        if start not in visited:
            visit(start)
            visited.append(start)
            for node in graph[start]:
                if node not in visited:
                    q.put(node)


def traverse_stack(graph, start, visit):
    """Przechodzenie w głąb z jawnym stosem"""
    stack = queue.LifoQueue()
    visited = []
    stack.put(start)
    while not stack.empty():
        start = stack.get()
        if start not in visited:
            visit(start)
            visited.append(start)
            for node in graph[start]:
                if node not in visited:
                    stack.put(node)
