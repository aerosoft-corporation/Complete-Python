# List Comprehension with if Statement

# Examples (Odd, Even)
# Without List Comprehension
nums = []
for i in range(1, 11):
    if i%2 == 0:
        nums.append(i)
print(nums)

# With list Comprehension
even_nums = [i for i in range(1, 11) if i%2 == 0]
print(even_nums)
odd_nums = [i for i in range(1, 11) if i%2 != 0]
print(odd_nums)