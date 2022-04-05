"""
Dijkstra’s shortest path algorithm is one algorithm of many that can be used to find the shortest path between two nodes of a graph.
* it generates a table that can be used to determine the shortest path between not only two specific nodes,
    but any two nodes that have an existing path between them within the graph.
* Greedy af, Dijkstra’s algorithm may not always be the most optimal solution to finding the shortest path between two nodes,
    but it makes up for these deficiencies with other benefits such as the fact that the algorithm only needs to be run once
    to determine the shortest between any two nodes in the graph as long as the graph remains unchanged.

Steps:
1. Begin at starting node, visit all adjacent nodes.
2. If distance is smaller than previously known smallest dist, update smallest dist and mark previous vertex
3. After all adjacent nodes have been visited, we mark starting node as visited.
4. We go to unvisited vertex with smallest known distance from starting node. (treat this as our new 'starting node' for current itteration
5. repeat 2-4 until all nodes are visited

(A)----[6]----(B)
 |           / |  \
 |         /   |   [5]
[1]     [2]   [2]     (C)
 |    /        |    [5]
 |  /          |  /
(D)----[1]----(E)

Code:
1. Dictionary with the key being the current vertex
2. 2 arrays, visited and unvisited
3.
    Begin iterating through the dictionary at the starting vertex. Check if the neighbors of the current vertex have been visited.
    If the neighbor hasn’t been visited, we keep track of the neighbor’s vertex name, distance to the neighbor, and current known cost to neighbor.
    Compare distance to the neighbor with the current known cost to the neighbor. If the distance to the neighbor is less than the current known cost, update the current known cost to the calculated distance. If not, leave the current known cost as is.
    After checking all neighbors of the current vertex, move the current vertex from the unvisited array to the visited array.
    Iterate through the unvisited array and find the unvisited node with the lowest known distance. Set the found node to the current node and repeat.
    Repeat the loop until the unvisited array is empty. Then return the table.

1. Graph Basics
2. BFS for Graphs
3. DFS for Graphs
4. Single Source Shortest Path in Undirected Graph
5. Cycle in an Undirected Graph
6. Cycle in Directed Graph
7. Topological Sorting
8. Shortest Path in Directed Acyclic Graph (DAG)
9. Minimum Spanning Tree (MST)
10. Dijkstra's Algorithm
11. Bellman Ford Shortest Path Algorithm
12. Kosaraju's Algorithm (Strongly Connected Component)
13. Tarjan's Algorithm (Strongly Connected Components
14. Articulation Point
15. Bridges in Graph
"""
import heapq
import math

graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}


graph2 = {
    "A": [("B", 6), ("D", 1)],
    "B": [("A", 6), ("D", 1), ("C", 5), ("E", 2)],
    "C": [("B", 5), ("E", 5)],
    "D": [("A", 1), ("E", 1), ("B", 2)],
    "E": [("D", 1), ("B", 2)]
}

def lazy_dijkstras2(graph, root):
    n = len(graph)
    # set up "inf" distances
    dist = [math.inf for _ in range(n)]
    # set up root distance
    dist[root] = 0
    # set up visited node list
    visited = [False for _ in range(n)]
    # set up priority queue
    pq = [(0, root)]
    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        _, u = heapq.heappop(pq)
        # if the node is visited, skip
        if visited[u]:
            continue
        # set the node to visited
        visited[u] = True
        # check the distance and node and distance
        for v, l in graph[u]:
            # if the current node's distance + distance to the node we're visiting
            # is less than the distance of the node we're visiting on file
            # replace that distance and push the node we're visiting into the priority queue
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))
    return dist


def lazy_dijkstras(graph: dict, root):
    n = len(graph)
    dist_dict = {}

    for index, key in enumerate(graph):
        dist_dict[key] = [index, math.inf, False]

    dist_dict[root][1] = 0


    # # set up "inf" distances
    # dist = [math.inf for i in range(n)]
    # # set up root distance
    # dist[root] = 0
    # # set up visited node list
    # visited = [False for i in range(n)]
    # set up priority queue
    #TODO!! here
    pq = [(0, root)]

    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        i, u = heapq.heappop(pq)
        # if the node is visited, skip
        # if dist_dict.get(u)[2]
        if dist_dict[u][2]:
        # if visited[u]:
            continue
        # set the node to visited
        dist_dict[u][2] = True
        # check the distance and node and distance
        for v, l in graph[u]:
            # if the current node's distance + distance to the node we're visiting
            # is less than the distance of the node we're visiting on file
            # replace that distance and push the node we're visiting into the priority queue
            if dist_dict[u][1] + l < dist_dict[v][1]:
            # if dist[u] + l < dist[v]:
                dist_dict[v][1] = dist_dict[u][1] + l
                # dist[v] = dist[u] + l
                # heapq.heappush(pq, (dist[v], v))
                heapq.heappush(pq, (dist_dict[v][1], v))
    return dist_dict

print(lazy_dijkstras(graph2, "A"))
print(lazy_dijkstras2(graph, 0))