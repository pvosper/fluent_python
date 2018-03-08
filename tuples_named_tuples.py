#!/usr/bin/env python
"""Example: 2-9"""

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

print(tokyo.population)

print(tokyo.coordinates)

print(tokyo[1])

# Example: 2-10

City._fields

LatLong = namedtuple('LatLong', 'lat long')
