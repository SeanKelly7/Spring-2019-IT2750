8.9
i. After a while it starts to rebuild the one rail decrypt that it started with and just no longer works
ii. in the odd numbers the spaces would be moved and some could be placed next to each other and would leave you with a large grouping of letters

8.14
def wordPop(text, n):
    nwords = []
    words = text.split()
    for word in words:
        if (len(word) == n):
             nwords.append(word)
    return (nwords)
    
w = 'This is a test for a length of words of different sizes'
print (wordPop(w.lower(), 5))

8.18
import re
expression = input("enter an expression: ")
print(re.findall(r'\b(\w+ing)\b',expression))

8.20
import re
expression = input("enter an expression: ")
print(re.findall(r'\b(A+\w+a)\b',expression))
