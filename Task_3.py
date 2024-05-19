import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

SG = nx.Graph() #Граф соціяальної мережі

user_nodes = ("Andrii","Igor", "Anton", "Julia", "Eugine", "Olya", "Mykola", "Nina", "Uljana")

# Додамо вагу ребер - кількість повідомлень між друзями
friend_edges = [
    ("Andrii", "Igor",3), ("Andrii", "Anton",5), ("Andrii", "Julia",2),
    ("Igor", "Julia",7), ("Igor", "Eugine",9), ("Igor", "Uljana",32),
    ("Anton", "Julia",23), ("Anton", "Olya",5), ("Anton", "Mykola",9),
    ("Julia", "Olya",22), ("Julia", "Mykola",17), ("Eugine", "Mykola",19),
    ("Eugine", "Nina",3), ("Eugine", "Andrii",35), ("Olya", "Mykola",12),
    ("Olya", "Uljana",7), ("Mykola", "Nina",5),
    ("Mykola", "Uljana",9), ("Nina", "Uljana",11)
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

SG.add_weighted_edges_from(friend_edges)


user_colors = ['blue', 'cyan', 'green', 'grey', 'magenta', 'orange', 'purple', 'red', 'yellow']
plt.figure(figsize=(12, 8))
nx.draw(SG, pos=user_positions, with_labels=True, node_color=user_colors, node_size=1000, edge_color='blue')
plt.title("Lviv online")
plt.show()


# Алгоритм Дейкстри
def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

graph_dict = {node: {neigh: attr['weight'] for neigh, attr in SG[node].items()} for node in SG.nodes()}


print()
print("Кількісь повідомлень між друзями")
print()
def format_dijkstra_results(results):
    table_data = []
    for start_vertex, paths in results.items():
        row = [f"Від {start_vertex}"]
        for target_vertex, distance in paths.items():
            if distance == float('infinity'):
                distance_str = "∞"
            else:
                distance_str = str(distance)
            row.append(distance_str)
        table_data.append(row)
    return table_data

all_paths = {vertex: dijkstra(graph_dict, vertex) for vertex in graph_dict}
table_data = format_dijkstra_results(all_paths)

headers = ["Вершина"] + [f"До {i}" for i in user_nodes]
print(tabulate(table_data, headers=headers, tablefmt="github", numalign="center"))