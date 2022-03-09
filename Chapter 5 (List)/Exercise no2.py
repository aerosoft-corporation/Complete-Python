# define a function wich will take list as a argument and this function will return a reversed list 

# Example
# [1, 2, 3, 4] ----> [4, 3, 2, 1]
# ['word1', 'word2'] ----> ['word2', 'word1']

# Note you simply do this with reverse method or [::-1]
# but try to do with help of append() and pop() method

# 1. Reverse Method
def reverse_list1(r1):
    r1.reverse()
    return r1

r1 = [1, 2, 3, 4]
total1 = reverse_list1(r1)
print("Reverse list1 With Reverse Method =", total1)


# 2. String Slicing [::-1]
def reverse_list2(r2):
    return r2[::-1]

r2 = [1, 2, 3, 4]
total2 = reverse_list1(r2)
print("Reverse list2 With Slicing =", total2)

# 3. Append() And Pop() Method
def reverse_list3(r3):
    rev = []
    for _ in range(len(r3)):
        popped_item = r3.pop()
        rev.append(popped_item)
    return rev

number = [1, 2, 3, 4]
total3 = reverse_list3(number)
print("Main Method =", total3)
