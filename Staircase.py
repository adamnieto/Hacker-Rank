#!/bin/python3

n = int(input().strip())
arr = []
for i in range(n):
    temp = ""
    temp += "#"*(i+1)
    arr.append(temp)

for i in arr:
    spaceCtr = n - len(i)
    newStr = i + " "*spaceCtr
    print(newStr[::-1])
