import collections # from collection dequeue
graph={
    "S": ["A","B","C"],
    "A": ["D"],
    "B": ["E","S"],
    "c": ["S","F","J"],
    "D": ["A","G","H"],
    "E": ["B","I","J"],
    "F": ["S","C"],
    "G": ["H","D"],
    "H": ["D","G"],
    "I": ["E"],
    "J": ["E"],
}

def main():
    print("entering the main function")
    node="S"
    outcome=bfs(graph,node)
def bfs(graph,node):
    visited_node=set()
    print("entering the bfs function")
    for checknodes in graph[node]:
        if checknodes not in visited_node:
            visited_node.add(checknodes)
    print(visited_node)
            

if __name__ == "__main__":
    main()


