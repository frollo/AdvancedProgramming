import es1

t = es1.Triangles(1)
c = es1.Circles(1)
r = es1.Rectangles(1,1)
s = es1.Squares(1)
p = es1.Pentagon(1)
h = es1.Hexagon(1)

print (s == r)
print (t < s)
print (c < r)
print (p > s)

print ([t,c,r,s,p,h])
print (sorted([t,c,r,s,p,h],key=lambda x: x.calculate_area()))
print (sorted([t,c,r,s,p,h],key=lambda x: x.calculate_perimeter()))
for a in es1.SortedAreas([t,c,r,s,p,h]):
    print (a)
