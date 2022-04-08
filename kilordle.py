from string import ascii_lowercase
from words import words, wordles
from string import ascii_lowercase
from pulp import LpVariable, const, LpProblem, LpMinimize, lpSum, LpStatus

letter_counts = {l: {i: sum(1 for w in wordles if w[i] == l) for i in range(5)} for l in ascii_lowercase}
needed = {l: {i for i, j in c.items() if j != 0} for l, c in letter_counts.items()}

problem = LpProblem("kilordle", LpMinimize)
all_words = words | wordles
variables = {w: LpVariable(w, 0, 1, const.LpInteger) for w in all_words}
problem += lpSum([variables[w] for w in all_words])

for letter, pos in needed.items():
    for i in pos:
        problem += lpSum([variables[w] for w in all_words if w[i] == letter]) >= 1

problem.solve()
print(LpStatus[problem.status])

best_words = {v.name for v in problem.variables() if v.varValue == 1}
print(f"Best solution has {len(best_words)} words: {', '.join(best_words)}")

sorted_words = [sorted(best_words, key=lambda w: w[i]) for i in range(5)]
print("\n".join(" ".join(sorted_words[i][j] for i in range(5)) for j in range(len(sorted_words[0]))))
