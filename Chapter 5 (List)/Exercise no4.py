# Filter Odd Even
# Define a function

# input
# list ----> [1,2,3,4,5,6,7,8]
# Output ----> [[1,3,5,7], [2,4,6,8]]

# Solution
def filter_odd_even(l):
    odd_nums = []
    even_nums = []
    for i in l:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    Output =  [odd_nums, even_nums]
    return Output

l = [1,2,3,4,5,6,7,8]
total = filter_odd_even(l)
print(f"Separate of Odd/Even {total}")