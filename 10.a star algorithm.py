import heapq

class Node:
    def __init__(self, state, parent=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.g_cost = g_cost  # Cost from the start node to this node
        self.h_cost = h_cost  # Heuristic cost from this node to the goal

    def __lt__(self, other):
        # Comparison function for priority queue
        return (self.g_cost + self.h_cost) < (other.g_cost + other.h_cost)

def astar(graph, start, goal, heuristic):
    open_set = [Node(start, None, 0, heuristic(start, goal))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state].items():
            if neighbor not in closed_set:
                g_cost = current_node.g_cost + cost
                h_cost = heuristic(neighbor, goal)
                new_node = Node(neighbor, current_node, g_cost, h_cost)

                if new_node not in open_set:
                    heapq.heappush(open_set, new_node)

    return None  # No path found

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': {'B': 10, 'C': 5},
        'B': {'A': 10, 'C': 2, 'D': 1},
        'C': {'A': 5, 'B': 2, 'D': 8},
        'D': {'B': 1, 'C': 8}
    }

    start_node = 'A'
    goal_node = 'D'

    def heuristic(node, goal):
        # Example heuristic function (Euclidean distance between nodes)
        return 0  # Replace with a proper heuristic function

    path = astar(graph, start_node, goal_node, heuristic)

    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
