1.>>>string = "The quick brown fox jumps over the lazy dog"
>>>list(string)
>>>string = list(string)
>>>string = [x.lower() for x in string]

2. >>>string.sort()
>>>string

3.string = [x for x in string if x != " "]
>>> def mode(stringlist):
...     countdict = {}
...     for ch in stringlist:
...         if ch in countdict:
...             countdict[ch] = countdict[ch] + 1
...         else:
...             countdict[ch] = 1
...     countlist = countdict.values()
...     maxcount = max(countlist)
...     modelist = []
...     for ch in countdict:
...         if countdict[ch] == maxcount:
...             modelist.append(ch)
...     return modelist
...
>>> mode(string)

4.
>>> def frequency(stringlist):
...     countdict = {}
...     for item in stringlist:
...         if item in countdict:
...             countdict[item] = countdict[item] +1
...         else:
...             countdict[item] = 1
...     itemlist = list(countdict.keys())
...     itemlist.sort()
...     for item in itemlist:
...         print(item)
...
>>> frequency(string)
