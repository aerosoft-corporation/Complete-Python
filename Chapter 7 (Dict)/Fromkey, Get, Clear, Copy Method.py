# 1. FromKeys() Method
# Note - If you want to give only one value to the multiple keys then we use fromkeys() method.
# Syntax
dic = dict.fromkeys(['name', 'age'], 'Unknown')
# dic1 = dict.fromkeys(range(1,11), 'Unknown')
print(dic)



# 2. Get() Mehtod
# If you want to access the value in dictionary then we use get() method
# Syntax 
user_info_1 = {
    'name' : 'Abbas',
    'age' : 21,
    'fav_movies' : ['The Martian', 'Rio'],
    'fav_Singer' : ['Edward Maya', 'Akcent']
}
# Old Method
print(user_info_1['name'])


# With get() method
print(user_info_1.get('name'))

# Benefit - Use the get() will not give us an error even if we put wrong key
# get() method with if, else condition

if user_info_1.get('name'):
    print('present')
    print(user_info_1.get('name'))
else:
    print('Not Present')



# 3. Clear() Method
# Note - Clear method is very simple method. this method is use for clear the dictionary
# Syntax
user_info_1.clear()
print(user_info_1)



# 4. Copy Method
# Note - copy() method is use for create a copy of a dictionary
# Right Syntax 
# This method will create a copy of your dictinary
copy = user_info_1.copy()    #Now these are two different dictionaries
print(copy is user_info_1)

# For Testing
print(f"Popped item from copy{copy.popitem()}")
print("Copy Method Now ", copy)
print(user_info_1)

# Wrong Syntax
# Note - This method will create a copy is is just simply stored in another variable
copy = user_info_1
print(copy is user_info_1)

# For Testing
print(copy.popitem())
print(user_info_1)