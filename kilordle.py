from string import ascii_lowercase
from words import words, wordles
from string import ascii_lowercase

letter_counts = {l: {i: sum(1 for w in wordles if w[i] == l) for i in range(5)} for l in ascii_lowercase}

missing = {l: {i for i, j in c.items() if j == 0} for l, c in letter_counts.items()}
#print({l: d for l, d in missing.items() if d != {}})

