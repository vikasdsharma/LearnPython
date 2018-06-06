# Program for the List Values to be Swapped

list_ex = ['Microsoft', 'Golden', 'Banana']
# This can be achieved with Simple code in python
def swap_ends(list1):
    print("List Values are As Follows")
    print(list1)
    a = list1.__len__()
    temp = list1[0]
    list1[0] = list1[a-1]
    list1[a-1] = temp
    print(list1)

swap_ends(list_ex)