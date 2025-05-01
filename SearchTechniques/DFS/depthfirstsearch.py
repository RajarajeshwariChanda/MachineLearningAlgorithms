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


def dfs(graph,node):
    visited_nodes=set()
    stack=[]
    ordered_dfs=list()
    stack.append(node)
    while stack:
        current_node=stack.pop()
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
            ordered_dfs.append(current_node)
            for next_node in reversed(graph[current_node]):
                stack.append(next_node)
    return ordered_dfs
            
    
    
def main():
    print("hey")
    output=dfs(graph,"S")
    print(output)
    
if __name__ == "__main__":
    main()
