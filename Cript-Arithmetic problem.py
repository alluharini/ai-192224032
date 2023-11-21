import itertools

def solve_cryptarithm(puzzle):
    # Separate the puzzle into words and the result
    words = puzzle.replace('+', ' ').replace('=', ' ').split()
    result_word = words[-1]
    words = words[:-1]

    # Create a list of unique letters in the puzzle
    letters = set(''.join(words + [result_word]))

    # Generate all possible permutations of digits for the letters
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        # Assign each digit to a letter
        digit_map = dict(zip(letters, perm))

        # Evaluate the puzzle with the current digit assignment
        numbers = [int(''.join(str(digit_map[c]) for c in word)) for word in words]
        result = int(''.join(str(digit_map[c]) for c in result_word))

        # Check if the puzzle is solved
        if sum(numbers) == result:
            return digit_map

    # If no solution is found, return None
    return None

# Example usage
puzzle = 'SEND + MORE = MONEY'
solution = solve_cryptarithm(puzzle)
if solution:
    for letter, digit in solution.items():
        print(f'{letter}: {digit}')
else:
    print('No solution found.')
