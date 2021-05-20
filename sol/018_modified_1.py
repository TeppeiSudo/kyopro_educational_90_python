import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

def get_location(L, T, time):
    theta = time/T * 2*math.pi
    cz = L/2
    y = -(L/2) * math.sin(theta)
    z = -(L/2) * math.cos(theta)
    return (0, y, cz+z)

for q in range(Q):
    e = int(input())
    _, y, z = get_location(L, T, e)
    length = math.sqrt(X**2 + (y-Y)**2)
    height = z
    ans = math.atan2(height, length)
    print(math.degrees(ans))