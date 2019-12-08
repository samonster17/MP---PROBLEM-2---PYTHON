from math import sqrt
x1 = int(input("input x1 = "))
y1 = int(input("input y1 = "))
x2 = int(input("input x2 = "))
y2 = int(input("input y2 = "))
x3 = int(input("input x3 = "))
y3 = int(input("input y3 = "))

a = x1*(y2-y3) - y1*(x2-x3) + (x2*y3) - (x3*y2)
b = (((x1**2)+(y1**2))*(y3-y2))+(((x2**2)+(y2**2))*(y1-y3))+(((x3**2)+(y3**2))*(y2-y1))
c = (((x1**2)+(y1**2))*(x2-x3))+(((x2**2)+(y2**2))*(x3-x1))+(((x3**2)+(y3**2))*(x1-x2))
d = (((x1**2)+(y1**2))*(((x3*y2)-(x2*y3)))) + (((x2**2)+(y2**2))*(((x1*y3)-(x3*y1)))) + (((x3**2)+(y3**2))*((x2*y1)-(x1*y2)))

#center point
x = -((b)/(2*a))
y = -((c)/(2*a))

#radius
r = sqrt(((b**2)+(c**2)-(4*a*d))/((4)*(a**2)))

# D E F
D = b/a
E = c/a
F = d/a

#eq'n
vector = [D, E, F]
print ("center = (", x, "," ,y,")")
print ("Radius = ", r)
print ("Vector [D,E,F] =", vector)