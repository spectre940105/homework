P=True
Q=False

from itertools import product

def generate_truth_table(variables, expression):
    header = " | ".join(variables + [expression])
    separator = "-" * len(header)
    
    print(header)
    print(separator)
    
    for assignment in product([False, True], repeat=len(variables)):
        assignment_dict = dict(zip(variables, assignment))
        result = eval(expression, assignment_dict)
        assignment_str = " | ".join(str(value) for value in assignment + (result,))
        print(assignment_str)