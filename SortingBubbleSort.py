n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
iteration = 0
# Track number of elements swapped during a single array traversal
numberOfSwaps = 0;
while iteration < n:
    j = 0
    while j < n - 1:
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            numberOfSwaps += 1

        j += 1

    
    # If no elements were swapped during a traversal, array is sorted
    if numberOfSwaps == 0:
        break
   
    iteration += 1

print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
