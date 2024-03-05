from math import radians, sin, cos, tan

angle = float(input('Type the value of angle: '))
rad = radians(angle)

s = sin(rad)
c = cos(rad)
t = tan(rad)

print('The angle radians value of {} is {}, its sine is {}, its cosine is {} and tangent is {}.'.format(angle, rad, s, c, t))
