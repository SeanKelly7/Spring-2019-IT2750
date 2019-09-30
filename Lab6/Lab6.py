7.1 
>>> num = 0
>>> while (num <=50):
...     print(num)
...     num = num + 5

7.2
>>> def spaces(string):
...     counter = 0
...     while (counter <= 0):
...             for a in string:
...                     if (a.count(' ')):
...                             counter = counter + 1
...             print(counter)
...
>>> spaces("hello monkey Man")

7.3
stopped = False
scores = []
sums = 0
average = 0
while (stopped == False):
    new_score = input ("Input a test score in, if you wish to stop type stop: ")
    if (new_score == "stop"):
        break
    scores.append(new_score)
scores = [int(i) for i in scores]
for i in scores:
    sums = sums + i
amount = len(scores)
average = sums / amount
print("the average of the scores is ")
print(average)

7.4
phrase = []
result = ""
pal = False
while (pal == False):
    string = input("input a word to see if its a palindrome: ")
    for i in reversed(string):
        result += i
    if (string == result):
        print("its a palindrome!")
        break
