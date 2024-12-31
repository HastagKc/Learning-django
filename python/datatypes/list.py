#  list
# collection of data in python (heterogenous)
# ordered
# mutable
# duplicate allow

# ordered
# list1 = ['kc', False, 12, {'bio': 'I am django developer'}]
# print(list1[0])
# print(list1[3])

# mutable
# list1[0] = "unnati"
# for i in list1:
#     print(i)


# duplicate allow
# Shallow Copy
# list1 = ['kc', False, 12, {'bio': 'I am django developer'}]
# list2 = list1

# list1address = id(list1)
# print(f'list one address -  {list1address}')
# list2address = id(list2)
# print(f'list two address -  {list2address}')

# list2[1] = "unnati"
# print(list1)
# print(list2)

# list3 = []
# list4 = []


list1 = ['kc', False, 12, {'bio': 'I am django developer'}]
list2 = list1.copy()

# address
list1address = id(list1)
print(f'list one address -  {list1address}')
list2address = id(list2)
print(f'list two address -  {list2address}')


list1[1] = "Ram"
print(list1)
print(list2)
