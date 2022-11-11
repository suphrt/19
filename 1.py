def f(s, p1, p2, c, m):
    if s >= 29:
        return c % 2 == m % 2
    if c > m:
        return 0

    if p1 == "+1":
        a = [f(s * 2, p2, "*2", c + 1, m), f(s + 2, p2, "+2", c + 1, m)]
    elif p1 == "+2":
        a = [f(s * 2, p2, "*2", c + 1, m), f(s + 1, p2, "+1", c + 1, m)]
    elif p1 == "*2":
        a = [f(s + 1, p2, "+1", c + 1, m), f(s + 2, p2, "+2", c + 1, m)]
    else:
        a = [f(s + 1, p2, "+1", c + 1, m), f(s + 2, p2, "+2", c + 1, m), f(s * 2, p2, "*2", c + 1, m)]

    if (c + 1) % 2 == m % 2:
        return any(a)
    else:
        return all(a)

for s in range(1, 29):
    for m in range(1, 10):
        if f(s, "", "", 0, m):
            print(s, m)
            break
