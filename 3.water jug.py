from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited_states = set()
    queue = deque([(0, 0, [])])  # Initial state with both jugs empty and an empty list to store steps

    while queue:
        current_state = queue.popleft()
        jug1, jug2, steps = current_state

        if current_state[:2] in visited_states:
            continue

        visited_states.add(current_state[:2])

        # Check if the target amount is reached
        if jug1 == target or jug2 == target:
            return steps + [(jug1, jug2)]

        # Pour water from jug1 to jug2
        if jug1 > 0:
            new_state = (max(0, jug1 - (jug2_capacity - jug2)), min(jug2 + jug1, jug2_capacity), steps + [(jug1, jug2, "Pour jug1 to jug2")])
            queue.append(new_state)

        # Pour water from jug2 to jug1
        if jug2 > 0:
            new_state = (min(jug1 + jug2, jug1_capacity), max(0, jug2 - (jug1_capacity - jug1)), steps + [(jug1, jug2, "Pour jug2 to jug1")])
            queue.append(new_state)

        # Empty jug1
        queue.append((0, jug2, steps + [(jug1, jug2, "Empty jug1")]))

        # Empty jug2
        queue.append((jug1, 0, steps + [(jug1, jug2, "Empty jug2")]))

        # Fill jug1 to its capacity
        queue.append((jug1_capacity, jug2, steps + [(jug1, jug2, "Fill jug1")]))

        # Fill jug2 to its capacity
        queue.append((jug1, jug2_capacity, steps + [(jug1, jug2, "Fill jug2")]))

    return None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

result = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

if result:
    print(f"Target amount of {target_amount} can be measured.")
    print("Steps:")
    for step in result:
        if len(step) == 2:
            print(f"({step[0]}, {step[1]})")
        elif len(step) == 3:
            print(f"({step[0]}, {step[1]}): {step[2]}")
        else:
            print("Invalid step format")
else:
    print(f"Target amount of {target_amount} cannot be measured.")
