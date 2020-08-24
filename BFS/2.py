# finding shortest path from source node to all other nodes and printing the path
#implementation of BFS traversal
from queue import Queue
visited = {}
level = {}
parent = {}
bfs_out = []
que = Queue()

def BFS(ad_list, src):

    for i in ad_list.keys():
        visited[i] = False
        parent[i] = None
        level[i] = -1

    visited[src] = True
    level[src] = 0
    que.put(src)

    while not que.empty():
        u = que.get()
        bfs_out.append(u)

        for v in ad_list[u]:
            if not visited[v]:
                visited[v] = True #ist line
                parent[v] = u # second line
                level[v] = level[u] + 1 # third line
                que.put(v)
    print(bfs_out)

# only when fully connected graph

def shortest_path(src, dest):
    path = []
    while dest is not None:
        path.append(dest)
        dest = parent[dest]
    path.reverse()
    print(path)

#main
ad_list = {
    "A" : ["B", "D"],
    "B" : ["A", "C"],
    "C" : ["B"],
    "D" : ["A", "E", "F"],
    "E" : ["D", "F", "G"],
    "F" : ["D", "E", "H"],
    "G" : ["E", "H"],
    "H" : ["G", "F"]
}

BFS(ad_list, "A")
shortest_path("A", "H")
