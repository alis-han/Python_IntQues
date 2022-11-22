#Take the angles x and y in degrees. Your task is to convert them to radian and compute the
#following expression. Print the result up to 2 decimal places at the end.
#  sin(x)cos(y) - cos(x)sin(y)

import math
rad=math.pi
a=int(input())
b=int(input())
x=a*(rad/180)
y=b*(rad/180)
output=(math.sin(x)*math.cos(y))-(math.cos(x)*math.sin(y))
print("{:.2f}".format(output))