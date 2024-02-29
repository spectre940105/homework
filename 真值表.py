from itertools import product
header = "P | Q | P∧Q | P∨Q |NotP∨NotQ|NotP∧NotQ| P→Q | P←Q | P↔Q"
separator = "-" * len(header)
    
print(header)
print(separator)
for assignment in product([False, True], repeat=2):
    P, Q = assignment
    result_and = P and Q
    result_or = P or Q
    result_xor=(not P) or (not Q)
    result_xnor=(not P) and (not Q)
    result_implies = (not P) or Q
    result_reverse_implies = P or (not Q)
    result_iff = P == Q
    
    row = f"{int(P)} | {int(Q)} |  {int(result_and)}  |   {int(result_or)}   |    {int(result_xor)}    |     {int(result_xnor)}    |  {int(result_implies)}  |  {int(result_reverse_implies)}  | {int(result_iff)}"
    print(row)