#!/usr/bin/env python
"""Example: 2-4
Contrast with listcomp_tshirts Ex 2-4"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# listcomp:
# tshirts = [(color, size) for color in colors for size in sizes]

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
