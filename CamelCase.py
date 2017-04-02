n = input().strip()
counter = 0
index = 0
for i in n:
    if i == i.lower() and index == 0:
        counter += 1
    if i == i.upper():
        counter += 1
    index += 1
print(counter)
