# Important Summary
# What is Dictionary
# Unordered Collection Of Data

# Example
# Method to create dictionary
# 1.
d = {'name' : 'abbas', 'age' : 21}

# 2. 
d1 = dict(name='Abbas', age=21)

# 3.
d2 = {
    'name' : 'Abbas',
    'age' : 21
}


# How to access data from dictonary
# You cannot do like list d[0] Because there is no indexing
# There is no indexing in dictionary

# Syntax
# print(dictname[key])
print(d['name'])


# Add Data, and Ad data in empty dictionary
empty_dict = {}
empty_dict['name'] = 'abbas'
empty_dict['age'] = 21
print(empty_dict)

# Check Existance of value inside dict
# Use in keyword to check for key
if 'name' in d:
    print('present')



# How to iterate over dictionary
# Most Common Method
for key, value in d.items():
    print(f"Key is {key}, Vlaue is {value}")



# For printing all keys
for i in d:
    print(i)

# Method 2.
for i in d.keys():
    print(i)



# For printing all values
for i in d.values():
    print(i)

# Method 2. 
for i in d:
    print(d[i])



# Most Common dict method to acces the key and check existance
print(d.get('age'))

# Q - Why we use get() Method 
# A - To get rid of Errors
print(d['name'])
print(d.get('name'))
# Note - If key Does not exist in dictionary the get() method will no give us error 
# print(d.get('names', 'Not Found'))  -  If key does not exist we can choose the statement for our error



# To Delete item in dictionary
# 1. pop() ---> Take one argument which is keyname
print('popoed item is ', d.pop('name'))
print(d)

# 2. Popitem() 
# Note - Randomly delete item from our dictionary
print(d.popitem())
print(d)


print('The End'.center(9, '*'))