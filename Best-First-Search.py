from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]
 
def best_first_search(source, target, n):
    visited = [0] * n
    visited[0] = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        
        if (u==source):
            print("Start", u, end="")
        else:
            print(" ->", u, end="")
        if u == target:
            break
 
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    
 
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
 

addedge(0, 1, 12)
addedge(0, 2, 4)
addedge(1, 3, 7)
addedge(1, 4, 3)
addedge(2, 5, 8)
addedge(2, 6, 2)
addedge(6, 7, 9)
addedge(6, 8, 0)

source = 2
target = 8
print("\nBest First Search\n")
best_first_search(source, target, v)
print()
