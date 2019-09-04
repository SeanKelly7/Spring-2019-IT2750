2.8
def First100EvenSum(num):
...     for i in range(2, 201, 2):
...             i = i + i
...     print(i)
Im not sure if thats how you wanted it but i was able to get it to work fine but you need to put in a random number for num

2.9
def First50OddSum(num):
...     for i in range (1, 100, 2):
...             i = i + i
...     print(i)

2.10
def First100Avg(num):
...     for i in range(1, 200, 2):
...             i = i + i
...     avg = i / 100
...     print(avg)
