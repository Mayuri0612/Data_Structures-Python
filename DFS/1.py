#implementation of DFS in a directed graph

# trav_time = {} #for other programs time will be used
#time = 0 
def DFS(u):
    color[u] = "G"
    dfs_output.append(u)

    for v in ad_list[u]:
        if color[v] == "W":
            parent[v] = u
            DFS(v)
    color[u] = "B"

ad_list1 = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["B", "F"],
    "D" : [],
    "E" : ["F"],
    "F" : []
}

ad_list = {
    "A" : ["B"],
    "B" : ["A","D", "E"],
    "C" : ["F"],
    "D" : ["B"],
    "E" : ["B"],
    "F" : ["C"]
}

#main function
color = {}
parent = {}
dfs_output = []
for i in ad_list.keys():
    color[i] = "W"
    parent[i] = None

for u in ad_list.keys():
    if color[u] == "W":
        DFS(u)
print(dfs_output)


