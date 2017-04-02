from collections import deque

def leftRotation(container):
    container.rotate(-shifts) #rotates the number of shifts '-' means left
    #prints contents in the correct format
    for num in container:
        print(num, end=' ')

#gets number of shifts from first line of input 
shifts = int(input().split()[1])
#gets array elements and then use library function to convert
#to a high performance container datatype
leftRotation(deque([int(i) for i in input().split()]))
