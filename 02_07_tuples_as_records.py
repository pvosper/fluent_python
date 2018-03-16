#!/usr/bin/env python
"""Example: 2-7"""

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]

print('\n% formatter understands tuples and treats each item as a separate field')
print('for passport in sorted(traveler_ids):')
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

print('\nfor loop knows how to retrieve the items of a tuple separately')
print('this is called _unpacking_')
print('for country, _ in traveler_ids:')
for country, _ in traveler_ids:
    print(country)
print('\nnote use of underscore as dummy variable')
