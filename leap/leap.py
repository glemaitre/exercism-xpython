def is_leap_year(y=1):
    _is_divisible = lambda x: y%x == 0

    answer = True if _is_divisible(4) else False
    answer = False if _is_divisible(100) else answer
    answer = True if _is_divisible(400) else answer

    return answer
