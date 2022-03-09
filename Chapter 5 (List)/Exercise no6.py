# counting the list inside list that how many list inside the list
# Example 
# input ----> [[1,2,3,], [4,5,6]]
# output ----> 2

# Solution
def list_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

l = [[1,2,3], [4,5,6]]
total = list_counter(l)
print(f"Total List are inside the list are {total}")