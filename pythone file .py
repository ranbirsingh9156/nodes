Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from sys import stdin


def rotate(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1

    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1

    arr[:] = arr[:i] + temp        
    #Your code goes here













... 
... 
... 
... 
... 
... 
... 
... 
... 
... 
... 
... 
... #Taking Input Using Fats I/O
... def takeInput() :
...     n = int(stdin.readline().rstrip())
...     if n == 0:
...         return list(), 0
... 
...     arr = list(map(int, stdin.readline().rstrip().split(" ")))
...     return arr, n
... 
... 
... #to print the array/list 
... def printList(arr, n) : 
...     for i in range(n) :
...         print(arr[i], end = " ")
...     print()
... 
... 
... #main
... t = int(stdin.readline().rstrip())
... 
... while t > 0 :
...     
...     arr, n = takeInput()
...     d = int(stdin.readline().rstrip())
...     rotate(arr, n, d)
...     printList(arr, n)
...     
