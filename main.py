from node import *
from graph import *
import json

with open("kevinbacon.json", "r") as file:
    data = json.load(file)

graph = Graph()
movies = data["movies"]
for i in range(len(movies)):
    title = movies[i]["title"]
    cast = movies[i]["cast"]
    movie_node = Node(title)
    graph.add_node(movie_node)

    for j in range(len(cast)):
        actor = cast[j]
        actor_node = graph.get_node(actor)
        if actor_node == None:
            actor_node = Node(actor)
        graph.add_node(actor_node)
        movie_node.add_edge(actor_node)

start = graph.set_start("Mark Ruffalo")
end = graph.set_end("Kevin Bacon")
graph.reset()

queue = list()
start.searched = True
queue.append(start)

while len(queue) > 0:
    current = queue.pop(0)
    if current == end:
        print("Found " + current.value)
        break
    edges = current.edges
    for nhb in edges:
        if not nhb.searched:
            nhb.searched = True
            nhb.parent = current
            queue.append(nhb)

path = list()
path.append(end)
nxt = end.parent
while nxt != None:
    path.append(nxt)
    nxt = nxt.parent

text = ""
for i in range(len(path)-1, -1, -1):
    text += path[i].value
    if i != 0:
        text += " --> "

print(text)
