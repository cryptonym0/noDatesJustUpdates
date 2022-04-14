# BFS Algorithm

As breadth-first search is the process of traversing each node of the graph, a standard BFS algorithm traverses each vertex of the graph into two parts: 
1) Visited 
2) Not Visited. 

So, the purpose of the algorithm is to visit all the vertex while avoiding cycles.

BFS starts from a node, then it checks all the nodes at distance one from the beginning node, then it checks all the nodes at distance two, and so on. So as to recollect the nodes to be visited, BFS uses a queue.

The steps of the algorithm work as follow:

1. Start by putting any one of the graph’s vertices at the back of the queue. 
2. Now take the front item of the queue and add it to the visited list. 
3. Create a list of that vertex's adjacent nodes. Add those which are not within the visited list to the rear of the queue.
4. Keep continuing steps two and three till the queue is empty.

# BFS Big O
**time complexity** O(Nodes + Edges). This is NOT O(n), nor is it O(nxm), it is O(n+m)

**space complexity:** O(Nodes).

## BFS: Data Structures Required:
- Queue
- List

## BFS Why Use? WHen Use?


1. In GPS navigation, it helps in finding the shortest path available from one point to another.
1. In pathfinding algorithms
1. Cycle detection in an undirected graph
1. In minimum spanning tree
1. To build index by search index
1. In Ford-Fulkerson algorithm to find maximum flow in a network.

## BFS pseudocode

The pseudocode for BFS in python goes as below:

```
create a queue Q
mark v as visited and put v into Q
while Q is non-empty
    remove the head u of Q
    mark and enqueue all (unvisited) neighbors of u
```

```python
#create a queue Q
visited = []
queue = []

def bfs(graph, starting_node):
    visited = []
    queue = []
#first node
    visited.append(starting_node)
    queue.append(starting_node)

    while queue:    #Create loop, visit each node
        current_node = queue.pop(0)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited
```