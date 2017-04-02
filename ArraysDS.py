n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
temp = ""
for i in arr[::-1]:
    temp += str(i) + " "
print(temp)
