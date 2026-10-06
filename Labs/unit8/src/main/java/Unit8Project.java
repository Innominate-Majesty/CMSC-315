/**
 * ============================================================
 * UNIT 8 PROJECT: CAMPUS NAVIGATION SYSTEM
 * ============================================================
 *
 * This project introduces graph data structures by modeling a
 * campus navigation system. Buildings are represented as vertices
 * (nodes) and walking paths between buildings are represented as
 * edges (connections). Students will create an undirected graph
 * using adjacency lists and explore how graph traversal can be
 * used to determine whether routes exist between locations.
 *
 * Learning Objectives:
 * - Understand how graphs model real-world navigation systems
 * - Represent graph data using a HashMap and adjacency lists
 * - Add and manage vertices (buildings) in a graph
 * - Create undirected connections between locations
 * - Implement Breadth-First Search (BFS) for pathfinding
 * - Use HashSet and Queue collections during graph traversal
 * - Practice problem solving with graph algorithms
 * - Create and run JUnit tests to validate graph behavior
 *
 * Real-World Applications:
 * - GPS and route planning systems
 * - Campus and building navigation tools
 * - Social network analysis
 * - Computer and communication networks
 * - Transportation and logistics systems
 *
 * Author: Venus Ho
 * Date: October 5, 2026
 * ============================================================
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class Unit8Project {

    public String getUnitName() {
        return "Unit 8 Project";
    }

    // Graph stores each building as a key and its neighbors as a list of connected buildings.
    private Map<String, List<String>> graph = new HashMap<>();

    public void addBuilding(String building) {
        // TODO (Student): Add the building to the graph.

        // TODO (Student): Make sure duplicate buildings are not added.        

        // if a building if it's not stored in the graph
        if (!graph.containsKey(building)) {

            // TODO (Student): Store the building with an empty neighbor list.

            // store the building with an empty list of neighboring buildings
            graph.put(building, new ArrayList<> ());
            
        }
    }

    public void addPath(String from, String to) {
        // TODO (Student): Ensure the starting building exists in the graph.
        // add the starting building if it doesn't already exist
        addBuilding(from);

        // TODO (Student): Ensure the destination building exists in the graph.
        // add the destination building if it doesn't already exist
        addBuilding(to);

        // TODO (Student): Add a path from the starting building to the destination building.
        // if the destination isn't already a neighbor of the starting building
        if (!graph.get(from).contains(to)) {

            // add a path from the starting building to the destination building
            graph.get(from).add(to);

        }

        // TODO (Student): Add a path from the destination building back to the starting building.
        // This graph is undirected, so paths must work in both directions.
        // if the starting building isn't already a neighbor of the destination building
        if (!graph.get(to).contains(from)) {

            // add the reverse path 
            // because this is an undirected graph
            graph.get(to).add(from);

        }

    }

    public List<String> getNeighbors(String building) {
        // TODO (Student): Return the list of neighboring buildings for the given building.

        // TODO (Student): Return an empty list if the building does not exist.

        // if the building exists in the graph
        if (graph.containsKey(building)) {

            // return the list of buildings connected to the requested building
            return graph.get(building);

        }

        // return an empty list when the requested building doesn't exist
        return new ArrayList<>();
    }

    public boolean hasPath(String start, String goal) {
        // TODO (Student): Return false if either building does not exist.

        // if the building is missing from the graph
        if (!graph.containsKey(start) || !graph.containsKey(goal)) {

            // return false
            return false;

        }

        // TODO (Student): Create a set to track visited buildings.

        // create a set to keep track of buildings that have already been visited
        Set<String> visited = new HashSet<>();

        // TODO (Student): Use Breadth-First Search (BFS) to determine whether a route exists.

        // TODO (Student): Create a queue to process buildings in BFS order.

        // create a queue to visit buildings in Breadth First search order
        Queue<String> queue = new LinkedList<>();

        // TODO (Student): Add the starting building to the queue and mark it as visited.

        // add the starting building to the queue
        queue.offer(start);

        // mark the starting building as visited
        visited.add(start);

        // TODO (Student): Continue searching while the queue is not empty.

        while (!queue.isEmpty()) {

            // TODO (Student): Remove the next building from the queue
            String currentBuilding = queue.poll();
            // TODO (Student): Return true if the current building is the goal.

            if (currentBuilding.equals(goal)) {

                return true;

            }


            // TODO (Student): Visit each unvisited neighbor and add it to the queue.

            // for each building connected to the current building
            for (String neighbor : graph.get(currentBuilding)) {

                // if the neighboring building hasn't been visited
                if (!visited.contains(neighbor)) {

                    // mark the neighboring building as visited
                    visited.add(neighbor);

                    // add the neighboring building to the queue for later searching
                    queue.offer(neighbor);

                }

            }
        
        }

        // TODO (Student): Return false if no route is found.

        return false;
    }

    public int size() {
        // TODO (Student): Return the number of buildings currently stored in the graph.

        return graph.size();
    }

    public static void main(String[] args) {
        Unit8Project app = new Unit8Project();

        // TODO (Student): Add the campus buildings.
        
        // add the Library to the graph
        app.addBuilding("Library");

        // add Science Hall to the graph
        app.addBuilding("Science Hall");

        // add the Gym to the graph
        app.addBuilding("Gym");

        // add the Cafeteria to the graph
        app.addBuilding("Cafeteria");

        // TODO (Student): Create walking paths between buildings.

        // create a walking path between the Library and Science Hall
        app.addPath("Library", "Science Hall");

        // create a walking path between Science Hall and the Gym
        app.addPath("Science Hall", "Gym");

        // create a walking path between the Gym and Cafeteria
        app.addPath("Gym", "Cafeteria");

        // TODO (Student): Verify the graph size.

        // print the total number of buildings stored in the graph
        System.out.println("Number of buildings: " + app.size());

        // TODO (Student): Display the neighbors of each building.

        // print every building connected directly to the Library
        System.out.println("Neighbors of Library: "
                + app.getNeighbors("Library"));

        // print every building connected directly to Science Hall
        System.out.println("Neighbors of Science Hall: "
                + app.getNeighbors("Science Hall"));

        // print every building connected directly to the Gym
        System.out.println("Neighbors of Gym: " + app.getNeighbors("Gym"));

        // print every building connected directly to the Cafeteria
        System.out.println("Neighbors of Cafeteria: " + app.getNeighbors("Cafeteria"));

        // TODO (Student): Test whether routes exist between buildings.

        // check and print if a route exists from the Library to the Gym
        System.out.println("Path from Library to Gym: "
                + app.hasPath("Library", "Gym"));

        // check and print if a route exists from the Library to the Cafeteria
        System.out.println("Path from Library to Cafeteria: "
                + app.hasPath("Library", "Cafeteria"));

        // check and print if a route exists from the Science Hall to the Gym
        System.out.println("Path from Science Hall to Gym: " + app.hasPath("Science Hall", "Gym"));

        // check and print if a route exists from the Gym to the Cafeteria
        System.out.println("Path from Gym to Cafeteria: " + app.hasPath("Gym", "Cafeteria"));

        // check and print the reverse direction to demonstrate that the graph is undirected
        System.out.println("Path from Cafeteria to Library: " + app.hasPath("Cafeteria", "Library"));

        // TODO (Student): Test a building that does not exist.

        // print and check a route that contains an unknown building
        System.out.println("Path from Library to Unknown: "
                + app.hasPath("Library", "Unknown"));
    }
}
