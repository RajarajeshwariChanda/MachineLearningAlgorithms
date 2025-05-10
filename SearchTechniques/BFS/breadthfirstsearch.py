# Step 0: Import necessary modules
import collections

# Step 1: Define the graph as an adjacency list
graph = {
    "S": ["A", "B", "C"],
    "A": ["D"],
    "B": ["E", "S"],
    "C": [ "F", "J","S"],
    "D": ["A", "G", "H"],
    "E": ["B", "I", "J"],
    "F": ["C","S"],
    "G": ["D","H"],
    "H": ["D", "G"],
    "I": ["E"],
    "J": ["E"]
}

# Step 2: Define the Breadth-First Search (BFS) function
def bfs(graph, start_node):
    # Step 3: Initialize data structures to keep track of visited nodes and BFS order
    visited_nodes = set()
    bfs_order = list()
    bfs_queue = collections.deque()
    
    # Step 4: Add the start node to the BFS queue
    bfs_queue.append(start_node)
    print("Entering the BFS function")
    
    # Step 5: Perform BFS traversal
    while bfs_queue:
        # Step 6: Dequeue the next node from the BFS queue
        current_node = bfs_queue.popleft()
        print("step 6 current node is :",current_node)
        
        # Step 7: Mark the current node as visited and add it to the BFS order
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
            print("step 7.1 visited node is:",visited_nodes)
        bfs_order.append(current_node)
        print("step 7.2 bfs order is :",bfs_order)
        
        # Step 8: Enqueue unvisited neighbors of the current node
        for next_node in graph[current_node]:
            if next_node not in visited_nodes:
                visited_nodes.add(next_node)
                print("step 8.1 visited node is:",visited_nodes)
                bfs_queue.append(next_node)
                print("step 8.2 bfs queue is :",bfs_queue)
                # Do not add neighbor to bfs_order here, it will be added when it is dequeued
    
    # Step 9: Print the BFS queue and order
    print("9.BFS queue:", bfs_queue)
    print("9.BFS order:", bfs_order)
    
    # Step 10: Return the BFS order
    return bfs_order

# Step 11: Define the main function
def main():
    print("Entering the main function")
    start_node = "S"
    bfs_result = bfs(graph, start_node)
    print("BFS result:", bfs_result)

# Step 12: Run the main function
if __name__ == "__main__":
    main()
