
#import modul
import random

print(random.randint (0,9))
print(random.randrange (1,10))

#import module
import math

#input number
angka = 9

#cari nilai akar
akar_angka = math.sqrt(angka)
print('akar dari ',angka,' adalah',akar_angka)

import cmath

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d)) / (2*a)
sol2 = (-b+cmath.sqrt(d)) / (2*a)

print('the solution are {0} and {1}'.format(sol1,sol2))

#tabel cosinus
from math import radians, sin, cos, tan
print ('menetukan nilai sin dan cos dari 0,30,60 - 360 derajat')
print ('sudut','\t','sin','\t','cos','\t','tan')
for i in range (0,361,30) :
    a=radians (i)
    b=sin (a)
    b=format (b,'.2f')
    c=cos (a)
    c=format (c,'.2f')
    d=tan (a)
    d=format (d,'.2f')
    print (i,'\t',b,'\t',c,'\t',d)
input('selesai')

#trigonometri
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar ==pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

#exponensial
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

#ceil and floor
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

#factorial
from math import factorial

x = 5

print(factorial(x))
