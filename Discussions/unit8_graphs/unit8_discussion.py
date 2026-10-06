"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Why a queue is used:
    ## BFS uses a queue because the first node added is the first node checked
    
    # Why neighbors are added to the queue:
    ## Neighbors are added to the queue so they can be visited after the current level

    # How BFS differs from depth first traversal:
    ## Unlike depth first traversal, BFS checks nearby nodes before moving farther away

    # if the starting node doesn't exist in the graph
    if start not in graph:

        # return an empty list 
        # because the traversal can't begin
        return []
    
    # create a set to keep track of nodes that have already been discovered
    visited = set()

    # create a queue and place the starting node inside it
    queue = deque([start])

    # mark the starting node as visited when it is added to the queue
    visited.add(start)

    # create an empty list to store the order in which nodes are visited
    traversal_order = []

    # continue searching while the queue contains nodes
    while queue:

        # remove the node that has been waiting in the queue the longest
        current_node = queue.popleft()

        # add the current node to the traversal order
        traversal_order.append(current_node)

        # for every neighbor connected to the current node
        for neighbor in graph.get(current_node, []):

            # if the neighboring node hasn't already been visited
            if neighbor not in visited:

                # mark the neighbor as visited so it's not added again
                visited.add(neighbor)

                # add the neighbor to the end of the queue to be visited later
                queue.append(neighbor)
    
    # return the traversal order
    return traversal_order

def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # print("TODO: Create and display a graph.")

    # each dictionary key represents a plant exhibit in the botanical garden
    # each list represents the exhibits connected by direct walking paths

    # create an empty dictionary for the botanical garden graph
    graph = {}

    # connect the Garden entrance to three nearby plant exhibits
    graph["Garden"] = ["Monstera", "Pothos", "Ghost Orchid"]

    # connect the Monstera exhibit to the entrance and two other exhibits
    graph["Monstera"] = ["Garden", "Jade Vine", "Pitcher Plant"]

    # connect the Pothos exhibit to the entrance and Moonflower exhibit
    graph["Pothos"] = ["Garden", "Moonflower"]

    # connect the Ghost Orchid exhibit to the entrance and Black Bat Flower Exhibit
    graph["Ghost Orchid"] = ["Garden", "Black Bat Flower"]

    # connect the Jade Vine exhibit to the Monstera and Corpse Flower
    graph["Jade Vine"] = ["Monstera", "Corpse Flower"]

    # connect the Corpse Flower exhibit to Jade Vine and Moonflower
    graph["Corpse Flower"] = ["Jade Vine", "Moonflower"]

    # connect the Black Bat Flower exhibit to Ghost Orchid and Dragon Tree
    graph["Black Bat Flower"] = ["Ghost Orchid", "Dragon Tree"]

    # connect the Pitcher Plant exhibit to Monstera and Dragon Tree
    graph["Pitcher Plant"] = ["Monstera", "Dragon Tree"]

    # connect the Moonflower exhibit to Pothos and Corpse Flower
    graph["Moonflower"] = ["Pothos", "Corpse Flower"]

    # connect the Dragon Tree exhibit to Pitcher Plant and Black Bat Flower
    graph["Dragon Tree"] = ["Pitcher Plant", "Black Bat Flower"]

    # for every plant exhibit and its connected exhibits
    for plant, connected_plants in graph.items():

        # print the plant exhibit and its direct walking paths
        print(plant + ":", connected_plants)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    # How BFS visits nodes level by level:
    ## BFS first visits the Garden and then the exhibits directly connected to it
    ## it continues level by level until every reachable plant exhibit is visited

    print("\n=== BFS TRAVERSAL ===")

    # print("TODO: Perform and explain BFS traversal.")

    # make the Garden entrance as the starting node
    starting_plant = "Garden"

    # perform BFS beginning at the Garden entrance
    traversal_order = bfs(graph, starting_plant)

    # print the starting location
    print("Starting node: ", starting_plant)

    # print the order in which the plant exhibits were visited
    print("BFS traversal order: ", traversal_order)

    # print the heading "UPDATED BFS TRAVERSAL"
    print("\n=== UPDATED BFS TRAVERSAL ===")

    # add a new Blue Puya exhibit connected to the Jade Vine exhibit
    graph["Blue Puya"] = ["Jade Vine"]

    # add the return path from Jade Vine to the new Blue Puya exhibit
    graph["Jade Vine"].append("Blue Puya")

    # print which new exhibit and walking path were added
    print("Added Blue Puya with a walking path to Jade Vine")

    # add a new Middlemist Red exhibit connected to the Ghost Orchid exhibit
    graph["Middlemist Red"] = ["Ghost Orchid"]

    # add the return path from Ghost Orchid to the new Middlemist Red exhibit
    graph["Ghost Orchid"].append("Middlemist Red")

    # print which new exhibit and walking path were added
    print("Added Middlemist Red with a walking path to Ghost Orchid")

    # add a new Rafflesia exhibit connected to the Corpse Flower exhibit
    graph["Rafflesia"] = ["Corpse Flower"]

    # add the return path from Corpse Flower to the new Rafflesia exhibit
    graph["Corpse Flower"].append("Rafflesia")

    # print which new exhibit and walking path were added
    print("Added Rafflesia with a walking path to Corpse Flower")

    # add a new Welwitschia exhibit connected to the Dragon Tree exhibit
    graph["Welwitschia"] = ["Dragon Tree"]

    # add the return path from Dragon Tree to the new Welwitschia exhibit
    graph["Dragon Tree"].append("Welwitschia")

    # print which new exhibit and walking path were added
    print("Added Welwitschia with a walking path to Dragon Tree")

    # add a new Juliet Rose exhibit connected to the Moonflower exhibit
    graph["Juliet Rose"] = ["Moonflower"]

    # add the return path from Moonflower to the new Juliet Rose exhibit
    graph["Moonflower"].append("Juliet Rose")

    # print which new exhibit and walking path were added
    print("Added Juliet Rose with a walking path to Moonflower")

    # perform BFS again after adding the five new exhibits
    updated_traversal_order = bfs(graph, starting_plant)

    # print the updated order in which the exhibits were visited
    print("Updated BFS traversal order: ", updated_traversal_order)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    
    # print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Start from a different node
    ## BFS begins at Dragon Tree instead of the Garden entrance
    ## it visits only the exhibits that can be reached from Dragon Tree
    
    # print the heading for edge case 1
    print("\nEdge Case 1: Start from a different node")

    # select Dragon Tree as the new starting node
    different_start = "Dragon Tree"

    # perform BFS from Dragon Tree
    different_start_result = bfs(graph, different_start)

    # print the traversal order from the different starting node
    print("Traversal from Dragon Tree:", different_start_result)

    # Edge case 2: Use a disconnected graph
    ## Ghost Orchid has no walking path connecting it to the other exhibits
    ## BFS cannot visit Ghost Orchid when the traversal begins at Garden

    # print the heading for edge case 2
    print("\nEdge Case 2: Use a disconnected graph")

    # create a graph containing one disconnected plant exhibit
    disconnected_graph = {
        "Garden": ["Monstera"],
        "Monstera": ["Garden"],
        "Ghost Orchid": []
    }

    # perform BFS on the disconnected graph
    disconnected_result = bfs(disconnected_graph, "Garden")

    # print the traversal order of the disconnected graph
    print("Disconnected graph traversal:", disconnected_result)

    # Edge case 3: Handle a missing start node safely
    ## Unknown Plant doesn't exist as a node in the graph
    ## the BFS function safely returns an empty list instead of causing an error

    # print the heading for edge case 3
    print("\nEdge Case 3: Handle a missing start node safely")

    # perform BFS with a starting node that doesn't exist
    missing_start_result = bfs(graph, "Unknown Plant")

    # print the result of using a missing starting node
    print("Missing start node traversal:", missing_start_result)

    # Edge case 4: Graph containing only one node
    ## Moonflower is the only node and doesn't have any neighbors
    ## BFS visits Moonflower once and then ends the traversal

    # print the heading for edge case 4
    print("\nEdge Case 4: Graph containing only one node")

    # create a graph containing only the Moonflower exhibit
    single_node_graph = {
        "Moonflower": []
    }

    # perform BFS on the single-node graph
    single_node_result = bfs(single_node_graph, "Moonflower")

    # print the traversal order of the single-node graph
    print("Single-node graph traversal:", single_node_result)

    # Edge case 5: Empty graph
    ## An empty graph doesn't contain any nodes or edges
    ## BFS returns an empty list because the starting node doesn't exist

    # print the heading for edge case 5
    print("\nEdge Case 5: Use an empty graph")

    # create an empty graph
    empty_graph = {}

    # perform BFS on the empty graph
    empty_graph_result = bfs(empty_graph, "Garden")

    # print the result of traversing the empty graph
    print("Empty graph traversal:", empty_graph_result)

    # Edge case 6: Graph containing a cycle
    ## Each plant connects to another plant in a path that returns to the first plant
    ## the visited set prevents BFS from repeating the cycle forever

    # print the heading for edge case 6
    print("\nEdge Case 6: Use a graph containing a cycle")

    # create a graph containing a cycle between three plant exhibits
    cycle_graph = {
        "Monstera": ["Pothos", "Ghost Orchid"],
        "Pothos": ["Monstera", "Ghost Orchid"],
        "Ghost Orchid": ["Pothos", "Monstera"]
    }

    # perform BFS on the graph containing a cycle
    cycle_result = bfs(cycle_graph, "Monstera")

    # print the traversal order of the graph containing a cycle
    print("Cycle graph traversal:", cycle_result)

    # Edge case 7: Node connected to itself
    ## Garden contains a walking path that points back to Garden
    ## the visited set makes sure Garden is visited only once

    # print the heading for edge case 7
    print("\nEdge Case 7: Use a node connected to itself")

    # create a graph containing a self-connection
    self_connection_graph = {
        "Garden": ["Garden", "Monstera"],
        "Monstera": ["Garden"]
    }

    # perform BFS on the graph containing a self-connection
    self_connection_result = bfs(self_connection_graph, "Garden")

    # print the traversal order of the graph containing a self-connection
    print("Self-connection traversal:", self_connection_result)

    # Edge case 8: Graph containing duplicate connections
    ## Monstera appears twice in Garden's neighbor list
    ## the visited set prevents Monstera from being added and visited twice

    # print the heading for edge case 8
    print("\nEdge Case 8: Use duplicate connections")

    # create a graph containing the same connection twice
    duplicate_connection_graph = {
        "Garden": ["Monstera", "Monstera"],
        "Monstera": ["Garden"]
    }

    # perform BFS on the graph containing duplicate connections
    duplicate_connection_result = bfs(duplicate_connection_graph, "Garden")

    # print the traversal order of the graph containing duplicate connections
    print("Duplicate-connection traversal:", duplicate_connection_result)

    # Edge case 9: Graph containing a one-way connection
    ## Garden can reach Monstera, but Monstera doesn't have a path back to Garden
    ## the traversal result changes depending on which node is used as the starting point

    # print the heading for edge case 9
    print("\nEdge Case 9: Use a one-way connection")

    # create a graph containing a one-way connection
    one_way_graph = {
        "Garden": ["Monstera"],
        "Monstera": []
    }

    # perform BFS from Garden through the one-way connection
    one_way_from_garden = bfs(one_way_graph, "Garden")

    # print the traversal beginning at Garden
    print("One-way traversal from Garden:", one_way_from_garden)

    # perform BFS from Monstera where no return path exists
    one_way_from_monstera = bfs(one_way_graph, "Monstera")

    # print the traversal beginning at Monstera
    print("One-way traversal from Monstera:", one_way_from_monstera)    



if __name__ == "__main__":
    main()
