#!/usr/bin/env python
# Example 2-15 'tuple' object does not support item assignment

t = (1, 2, [30, 40, 50, 60])
t[2] += [50, 60]

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /Users/paulvosper/Projects/fluent_python/02_15_+=_assignment_puzzler.py in <module>()
#       3
#       4 t = (1, 2, [30, 40, 50, 60])
# ----> 5 t[2] += [50, 60]
#
# TypeError: 'tuple' object does not support item assignment

t
# Out[4]: (1, 2, [30, 40, 50, 60, 50, 60])

# See: pythontutor.com to vizualize how python works in detail