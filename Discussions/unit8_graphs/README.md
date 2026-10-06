# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

--> The concept that I learned while completing this assignment is how to create a graph from scratch. I learned that each node can represent a location, while the connections between nodes can represent paths. I also learned how to organize several connected locations so that the program can move from one node to another. Another concept I learned was how to implement Breadth-First Search (BFS). BFS uses a queue to visit the closest connected nodes before moving farther away from the starting point. I also learned how to use a Python dictionary to represent these concepts by storing each node as a key and its connected neighbors as a list. This assignment helped me understand how graphs, dictionaries, queues, and visited sets worked together.

2. What challenges did you encounter, and how did you overcome them?

--> One of the challenges I encountered was deciding which theme to use for the graph. After choosing a botanical garden, I had some difficulty selecting the pants that would be included. Although I know several indoor and household plants, I wanted the program to feel more like a botanical garden that someone could visit. I chose a mixture of familiar plants and rare or uncommon plants that were still recognizable and easy to understand. Another challenge was thinking of useful edge cases that were different from the examples provided in the starter code. I added cases involving cycles, self connections, duplicate connections, and one way paths that see how BFS would respond. Testing these situations helped me understand why the visited set is important and made me more confident that the BFS function worked correctly.

3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

--> BFS and DFS both explore the nodes in a graph but they follow different paths through the data. BFS visits the closest connected nodes first and then continues to locations that are farther away. DFS follows one path as far as possible before returning to explore a different path. BFS is useful for finding the shortest route in an unweighted map, located nearby people in a social network, or exploring nearby exhibits in a botanical garden. DFS can be useful for exploring mazes, searching folders and files, or checking every part of a connected system. For this assignment, BFS was the better choice because it allowed the program to visit the closest plant exhibits before moving deeper into the garden. Both methods are useful but the best choice depends on the order in which the program needs to explore the graph.

