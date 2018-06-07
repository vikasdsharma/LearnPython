# This is for the While Loop understanding purpose only.

total = 0
i = 0
while i < 10:
    total += i
    i += 1
print(total)

given_list = [5, 4, 4, 23, 1, 11, -1, -4, -5]
j = 0
while given_list[j] > 0:
    print("This is a positive number ", given_list[j])
    j += 1

k = 0
totals = 0
while True:
    totals += given_list[k]
    k += 1
    if given_list[k] < 0:
        break
print("Total :  ", total)

# Problem Solution in Loop

given_list2 = [0, 2, 3, 4, 5, 6, 7, 8, -8, -7, -6, -5, -4, -3, -2, -1]
li = len(given_list2) - 1
totalm = -1
totalm = 0
while given_list2[li] < 0:
    totalm += given_list2[li]
    print("Total In Mid Calc : ", totalm)
    print(given_list2[li])
    li -= 1
print("Sum of all Negatives :   ", totalm)