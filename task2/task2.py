import sys

def check (x,y,x0,y0,r):
    a = (float(x) - float(x0)**2) + (float(y) - float(y0))**2
    b = float(r)**2
    if a < b:
        print(1)
    elif a == b:
        print(0)
    else: print(2)

circle = open(sys.argv[1], 'r').read()
xy0,r = [i for i in circle.rsplit('\n') if i != '']
x0,y0 = xy0.rsplit(' ')

points = open(sys.argv[2], 'r').read().rsplit('\n')
points = [i.rsplit(' ') for i in points if i != '']

for point in points:
    check(point[0],point[1],x0,y0,r)


