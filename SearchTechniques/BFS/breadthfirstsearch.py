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
    outcome=bfs()
def bfs():
    print("entering the bfs function")

if __name__ == "__main__":
    main()


