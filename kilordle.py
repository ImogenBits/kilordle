from string import ascii_lowercase
from words import words, wordles
from string import ascii_lowercase
from pulp import LpVariable, const, LpProblem, LpMinimize, lpSum

letter_counts = {l: {i: sum(1 for w in wordles if w[i] == l) for i in range(5)} for l in ascii_lowercase}

needed = {l: {i for i, j in c.items() if j != 0} for l, c in letter_counts.items()}
#print({l: d for l, d in missing.items() if d != {}})

problem = LpProblem("kilordle", LpMinimize)
variables = {w: LpVariable(w, 0, 1, const.LpInteger) for w in words}
problem += lpSum([variables[w] for w in wordles])

for letter, pos in needed.items():
    for i in pos:
        problem += lpSum([variables[w] for w in wordles if w[i] == letter]) >= 1

status = problem.solve()

print(status)

print(123)
