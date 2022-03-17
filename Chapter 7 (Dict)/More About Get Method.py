# Get() Mehtod
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



#  >>>> Some More Work with get() Method 
print(user_info_1.get('name'))

# Note - If key does not exist in the dictionary. The get() Method will declare (None).-
# But if you want anyother output try this
print(user_info_1.get('names', 'Not Found'))    #The output will be "Not Found" if the key does not exist.


# Note - 
# If two key (with the same name) Exist in the dictionary. The new one will overwrite the previous one
# Example 
example = {
    'name' : 'abbas',
    'age' : 21,
    'age' : 22
}
print(example.get('age'))
print(example['age']) 
# Output will be (22) of both statement, because the new same key will overwrite the previous one