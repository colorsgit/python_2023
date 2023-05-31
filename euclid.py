e = 43
f = 60

a = f
b = e
qs = []
while b != 0:
    q = a // b
    r = a % b

    qs = [q] + qs

    a = b
    b = r

# x' = qx + y
# y' = x

# x = y'
# y = x' - qx

x = 1
y = 0
for q in qs:
    #_x, _y = x, y
    #x = _y
    #y = _x - q * x
    x = y
    y = x - q * x

d = y

print(d)
