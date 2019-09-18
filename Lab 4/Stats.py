>>> def mean(list):
...     mean = sum(list) / len(list)
...     return mean
...
>>> mean([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])

>>> def median(alist):
...     copylist = alist[:] # make a copy using slice operator
...     copylist.sort()
...     if len(copylist)%2 == 0: # even length
...         rightmid = len(copylist)//2
...         leftmid = rightmid - 1
...         median = (copylist[leftmid] + copylist[rightmid])/2
...     else:    #odd length
...         mid = len(copylist)//2
...         median = copylist [mid]
...     return median
...
>>> median([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])

