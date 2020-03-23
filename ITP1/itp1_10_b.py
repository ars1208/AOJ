import math

a, b, C = map(float,input().split())

S = 0.5 * a * b * math.sin(math.radians(C))
l = (a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))**0.5 + a + b
h = (2 * S) / a

print(S)
print(l)
print(h)
