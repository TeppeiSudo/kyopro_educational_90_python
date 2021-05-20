import math

pi = math.pi

def query(time):
    cx = 0
    cy = -(L/2) * math.sin(time/T * 2*pi)
    cz = (L/2) - (L/2) * math.cos(time/T * 2*pi)
    d1 = math.sqrt((cx-X)**2 + (cy-Y)**2)
    d2 = cz
    kaku = math.atan2(d2, d1)
    return kaku * 180/pi

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for i in range(Q):
    E = int(input())
    print(query(E))