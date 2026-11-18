

def solve(value):
    return (lambda s: s == s[::-1])(''.join(c for c in value.casefold() if c.isalnum()))
