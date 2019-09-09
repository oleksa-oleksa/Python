def get_fib_loop(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    first = 0
    second = 1
    nextt = first + second
    i = 0
    while i < position:
        first = second
        second = next
        nextt = first + second
        i += 1
    return nextt
