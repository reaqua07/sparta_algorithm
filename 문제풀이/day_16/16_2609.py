a, b = map(int, input().split())

temp = 0

if a > b:
    a = a
elif a < b:
    temp = a
    a = b
    b = temp


def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a % b)


def LCM(a, b):
    g = GCD(a, b)
    return (g * (a / g) * (b / g))


print(GCD(a, b))
print(int(LCM(a, b)))
