# Common Method To Delete Data From List

# 1. Pop Method
# If You Do Not Pass Any Element Position Then Pop Method Will Remove The Last Element Automatically
Fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']
Fruits.pop(0)
Fruits.pop()
print(f'Pop Method >>>  {Fruits}')


# 2. Delete Operator
Fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']
del Fruits [1]
print(f'Delete Operator >>>  {Fruits}')


# 3. Remove Method 
# If We Don't Know Position Of Particular Element Then We Can Use Remove Method To Remove Element By \n
# Writing Element Name
Fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']
Fruits.remove("Banana")
print(f"Remove Method >>>  {Fruits}")