"""Write a program that will allow the user to:
    Add new definitions
    Search existing definitions
    Delete the definition that he has chosen"""
dictinory = {}
print(dictinory)

print("1: Add definition")
print("2: search for definition")
print("3: Remove definition")
print("4: End")

choice = input("What do you want to do? ")
if (choice == "1"):
    key = input("Enter the word (key) to define: ")
    definition = input("Enter Definition")
    dictinory[key] = definition
    print("Definition added successfully")
    print(dictinory)
    print(dictinory["abcd"])

def func(name):
    print("Hello", name, "Welcome home!")
names = ["shaher", "umar", "kamar"]
for name in names:
    func(name)


def rectangle(len, brt):
    print(len * brt)
rectangle(2,4)

def rectangle(len, brt):
    return len * brt
abc = rectangle(2,9)
print(abc)

def divide_zero(a,b):
    if (b==0):
        return "kuch nhi"
    return a/b
print(divide_zero(20,0))

n = 6
sum = 0
for i in range(1, n):
    sum = sum+i
    print(sum)
print(sum)

def sum_karo():
    n = 6
    sum = 0
    for i in range(1, n):
        sum = sum + i
        return sum
    return sum
print(sum_karo())

def sum_karo2(n):
    return sum([number for number in range(1,n)])
print(sum_karo2(6))

numbers = [1,2,3,4,5]
powernumbered = []
for i in numbers:
    powernumbered.append(i**2)
print(powernumbered)

powernum2 = [i**2 for i in numbers]
print(powernum2)

names= {"alas", "palas", "chals", "khalas", "narmada", "parhs"}
namesLenghth = {
    name : len(name)
    for name in names
}

list1 = [2,4,6,8,9]
list2 = [11,12,13,14]


# Append is used to add value at the end of list#
list1.append(10)
# Insert is used to add value at specific index location#
list1.insert(2,5)
# Extend is used to add another list with already existing list.. like we have add list 2 in list 1.
list1.extend(list2)
list1.reverse()
list1.sort()
# Reverse=True is used to sort list in desending order.
list1.sort(reverse=True)

sorted_without_disturbing_original_list=sorted(list1)
# print(sorted_without_disturbing_original_list)
print(list1)

# find out the index of particular value#
print(list1.index(2))

# Enumerate is used to get the index number and the value.
for index, number in enumerate(list1, start=1):
    print(index, number)

# convert list into string with the help of (join)
now = ["Aman", "Raman", "Chaman", "Gulam"]
now_str = ' - '.join(now)
print(now_str)

# back to the real list value
back_to_original_list = now_str.split(' - ')
print(back_to_original_list)

# Empty list

list = []
empty_list = list()

# Empty tuple
tuple = ()
empty_tuple = tuple()

set = {} ----"""This is not empty set! This is empty dictinory"""
empty_set = set()