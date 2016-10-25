def distance(s1, s2):
    diff = [1 for (a,b) in zip(s1, s2) if a!=b]
    return sum(diff)
