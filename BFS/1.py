#implementation of BFS traversal
from queue import Queue
def BFS(ad_list, src):
    visited = {}
    level = {}
    parent = {}
    bfs_out = []
    que = Queue()

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
