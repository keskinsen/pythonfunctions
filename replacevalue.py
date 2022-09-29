# -*- coding: utf-8 -*-


x = 10
y = 20

# print("x =" + str(x))
# print("y =" + str(y))

x = str(x)
y = str(y)

print("x =" + x.replace(x, y),"y =" + x.replace(y, x))
# print("y =" + x.replace(y, x))

#alternatif

# temp = x
# x=y
# y=temp

# #alternatif3

# x,y= y,x



