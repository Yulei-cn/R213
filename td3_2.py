c0 = 300
m = 45
t = 2.3
n = 8

def c(n):
    if n == 0:
        return c0
    else:
        return ((c(n - 1) + m) * (1 + t / 100 / 12))


print("Le capital obtenu après", n, "ans est de", round(c(n * 12), 2), "€")
print("Les intérêts gagnés après", n, "ans sont de", round(c(n * 12) - (n * 12 * m) - c0, 2), "€")
print("Sans intérêts, le total serait de", n * 12 * m + c0, "€")
