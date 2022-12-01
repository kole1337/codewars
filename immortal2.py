def elder_age(m,y,l,t):
    T = 0
    while y:
        y, Y, x = y & y-1, y, m
        while x:
            x, X = x & x-1, x
            s, S = sorted((X - x, Y - y))
            h = max((x^y | S-1) + 1 - l, 0)
            w = min(h, S)
            T += s * w * (h + h - w - 1) // 2
    return T % t

#https://www.codewars.com/kata/59568be9cc15b57637000054/train/python