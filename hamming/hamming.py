def distance(s1, s2):
    pairs = zip(s1, s2)
    equal = [p[0]==p[1] for p in pairs]
    _d = 0
    for e in equal:
        if not e:
            _d += 1
    return _d
