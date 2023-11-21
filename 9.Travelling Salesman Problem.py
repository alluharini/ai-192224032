from itertools import permutations

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(graph):
    num_cities = len(graph)
    cities = list(range(num_cities))

    # Generate all possible permutations of cities
    all_paths = permutations(cities)

    min_distance = float('inf')
    optimal_path = None

    for path in all_paths:
        distance = calculate_total_distance(path, graph)
        if distance < min_distance:
            min_distance = distance
            optimal_path = path

    return optimal_path, min_distance

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    optimal_path, min_distance = traveling_salesman_bruteforce(graph)

    print("Optimal TSP Path:", optimal_path)
    print("Minimum Distance:", min_distance)
