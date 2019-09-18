>>> def mean(list):
...     mean = sum(list) / len(list)
...     return mean
...
>>> mean([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])

>>> def median(medianlist):
...     copy = medianlist[:] # make a copy using slice operator
...     copy.sort()
...     if len(copy)%2 == 0: # even length
...         rightmid = len(copy)//2
...         leftmid = rightmid - 1
...         median = (copy[leftmid] + copy[rightmid])/2
...     else:    #odd length
...         mid = len(copy)//2
...         median = copy [mid]
...     return median
...
>>> median([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])

>>> def mode(modelist):
...     counts = {}
...
...     for item in modelist:
...         if item in counts:
...             counts[item] = counts[item]+1
...         else:
...             counts[item] = 1
...
...     countlist = counts.values()
...     maxcount = max(countlist)
...
...     modelist = []
...     for item in counts:
...         if counts[item] == maxcount:
...             modelist.append(item)
...
...     return modelist
...
>>> mode([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])
