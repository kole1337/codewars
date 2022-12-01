import re

def expand(expr):
    a, x, b, n = re.match(r'\((.*)(\D)([+-].+)\)\^(\d+)', expr, re.I).groups()
    poly, c, a, b, n = {}, 1, int(a.rstrip('-') or a + '1'), int(b), int(n)
    for r in range(n + 1):
        c = c * (n - r + 1) // (r or n + 1)
        poly[n - r] = c * a ** (n - r) * b ** r
    return re.sub(r'(?<=[+-])1(?=\D)', '',
                  ''.join('{:+d}{}^{}'[:7 + 3 * (p > 1)].format(r, x, p)
                          for p, r in poly.items()).rstrip(x), re.I).lstrip('+')