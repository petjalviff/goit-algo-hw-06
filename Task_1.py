import networkx as nx
import matplotlib.pyplot as plt

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

user_colors = ['blue', 'cyan', 'green', 'grey', 'magenta', 'orange', 'purple', 'red', 'yellow']
plt.figure(figsize=(12, 8))
nx.draw(SG, pos=user_positions, with_labels=True, node_color=user_colors, node_size=1000, edge_color='blue')
plt.title("Lviv online")
plt.show()

total_users = SG.number_of_nodes()
total_friendships = SG.number_of_edges()
user_degrees = dict(SG.degree())

print("Кількість користувачів - ", total_users)
print("Кількість зв'язків - ", total_friendships)
print("Ступені користувачів: ", {f"Користувач {user}": degree for user, degree in user_degrees.items()})