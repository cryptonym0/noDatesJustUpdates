# DFS Algorithm
The Depth-First Search is a recursive algorithm that uses the concept of backtracking. It involves thorough searches of all the nodes by going ahead if potential, else by backtracking. Here, the word backtrack means once you are moving forward and there are not any more nodes along the present path, you progress backward on an equivalent path to seek out nodes to traverse. All the nodes are progressing to be visited on the current path until all the unvisited nodes are traversed after which subsequent paths are going to be selected.

The recursive method of the Depth-First Search algorithm is implemented using stack. A standard Depth-First Search implementation puts every vertex of the graph into one in all 2 categories: 1) Visited 2) Not Visited. The only purpose of this algorithm is to visit all the vertex of the graph avoiding cycles.

The DSF algorithm follows as:

1. We will start by putting any one of the graph's vertex on top of the stack.
2. After that take the top item of the stack and add it to the visited list of the vertex.
3. Next, create a list of that adjacent node of the vertex. Add the ones which aren't in the visited list of vertexes to the top of the stack.
4. Lastly, keep repeating steps 2 and 3 until the stack is empty.

## DFS Big O

**time complexity** O(Nodes + Edges). This is NOT O(n), nor is it O(nxm), it is O(n+m)

**space complexity:** O(Nodes).

## DFS: Data Structures Required:
- Stack (Set)
- List
- Concept: recursion
- Memoization?

## DFS: Why Use? When Use?

1. For finding the strongly connected components of the graph 
2. For finding the path
3. To test if the graph is bipartite
4. For detecting cycles in a graph
5. Topological Sorting 
6. Solving the puzzle with only one solution.
7. Network Analysis
8. Mapping Routes
9. Scheduling a problem

## DFS pseudocode

The pseudocode for BFS in python goes as below:

```
where G = Graph and u = unvisited
DFS(G, u)
    u.visited = true
    for each v ∈ G.Adj[u]
        if v.visited == false
            DFS(G,v)   

init() {
    For each u ∈ G
        u.visited = false
     For each u ∈ G
       DFS(G, u)
}
```

## DFS Code
```python

def dfs(visited_set, graph, current_node):
    if current_node not in visited_set:
        visited_set.add(current_node)
        
        for neighbour in graph[current_node]:
            #recusion time!
            dfs(visited_set, graph, neighbour)
    return visited_set
            
def init(graph):
    visited_set = set()
    
    for node in graph:
        dfs(visited_set, graph, node)

```