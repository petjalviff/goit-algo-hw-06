import networkx as nx
from collections import deque

SG = nx.Graph() #Граф соціяальної мережі

user_nodes = ("Andrii","Igor", "Anton", "Julia", "Eugine", "Olya", "Mykola", "Nina", "Uljana")

friend_edges = [
    ("Andrii", "Igor"), ("Andrii", "Anton"), ("Andrii", "Julia"),
    ("Igor", "Julia"), ("Igor", "Eugine"), ("Igor", "Uljana"),
    ("Anton", "Julia"), ("Anton", "Olya"), ("Anton", "Mykola"),
    ("Julia", "Olya"), ("Julia", "Mykola"), ("Eugine", "Mykola"),
    ("Eugine", "Nina"), ("Eugine", "Andrii"), ("Olya", "Mykola"),
    ("Olya", "Uljana"), ("Mykola", "Nina"),
    ("Mykola", "Uljana"), ("Nina", "Uljana")
]

user_positions = {
    "Andrii": [-1.0, 0.05],
    "Igor": [-0.55, -0.919],
    "Anton": [-0.644, 0.644],
    "Julia": [-0.373, 0.126],
    "Eugine": [0.261, -0.905],
    "Olya": [0.132, 0.941],
    "Mykola": [0.091, -0.143],
    "Nina": [0.718, -0.388],
    "Uljana": [0.768, 0.292]
}

SG.add_nodes_from(user_nodes)
SG.add_edges_from(friend_edges)

dict_graph = nx.to_dict_of_lists(SG)
print(dict_graph)

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    dfs_result = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            dfs_result.append(vertex)
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
    return dfs_result

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    bfs_result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            bfs_result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return bfs_result

dfs_result = dfs_iterative(dict_graph, "Anton")
bfs_result = bfs_iterative(dict_graph, "Anton")

print("Ітеративний пошук в глибину (DFS):", ", ".join(map(str, dfs_result)))
print("Ітеративний пошук в ширину (BFS):", ", ".join(map(str, bfs_result)))