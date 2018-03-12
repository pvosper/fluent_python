#!/usr/bin/env python
"""Example: 2-9 Named Tuples"""

"""The collections.namedtuple function is a factory that produces subclasses of
    tuple enhanced with field names and a class name - which helps debugging"""


from collections import namedtuple

"""Two parameters are required to create a named tuple: a class name and a list of field names
    which can be given as an iterable of string or as a single space delimited string"""

City = namedtuple('City', 'name country population coordinates')

"""Data must be passed as positional arguments to the constructor"""
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

tokyo
# Out[5]: City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))

"""You can access the fields by name or position"""
tokyo.population
# Out[6]: 36.933

tokyo.coordinates
# Out[7]: (35.689722, 139.691667)

tokyo[1]
# Out[8]: 'JP'

"""Example: 2-10 Named tuple attributes and methods, continued"""

"""_fields is a tuple with the field name s of the class"""
City._fields
# Out[2]: ('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
dehli_data = ('Dehli NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
"""_make() allow you to instantiate a named yuple from an iterable;
    City(*delhi_data) would do the same"""
dehli = City._make(dehli_data)
dehli._asdict()
# Out[12]:
# OrderedDict([('name', 'Dehli NCR'),
#              ('country', 'IN'),
#              ('population', 21.935),
#              ('coordinates', LatLong(lat=28.613889, long=77.208889))])

"""_asdict() returns a collections.OrderedDict built from the named tuple 
    instance. That can be used to produce a nice display of city data"""
for key, value in dehli._asdict().items():
    print(key + ':', value)

# name: Dehli NCR
# country: IN
# population: 21.935
# coordinates: LatLong(lat=28.613889, long=77.208889)