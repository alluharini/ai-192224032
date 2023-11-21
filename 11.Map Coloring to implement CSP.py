class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, variable, value):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack_search(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment  # Solution found

        variable = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(variable, assignment):
            if self.is_consistent(assignment, variable, value):
                assignment[variable] = value
                result = self.backtrack_search(assignment)
                if result is not None:
                    return result
                del assignment[variable]

        return None  # No solution found

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def order_domain_values(self, variable, assignment):
        return self.domains[variable]

# Example usage:
if __name__ == "__main__":
    # Variables represent regions, and domains represent possible colors
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['R', 'G', 'B'] for var in variables}

    # Constraints represent neighboring regions that cannot have the same color
    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }

    csp = CSP(variables, domains, constraints)
    assignment = csp.backtrack_search({})

    if assignment:
        print("Solution found:")
        for variable, value in assignment.items():
            print(f"{variable}: {value}")
    else:
        print("No solution found.")
