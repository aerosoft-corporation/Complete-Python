user_info_ = {
    'name' : 'Abbas Ali',
    'age' : 21,
    'fav_movies' : ['The Martian', 'Rio'],
    'fav_Singer' : ['Edward Maya', 'Akcent']
}

# 1. Add Data in Dict

# user_info_['City'] = 'Shinkiari'    # This method will Add Data in your dictionary
# print(user_info_)


# 2. Pop() Method

popped_item = user_info_.pop('name')    #This method will also return the popped item
# print(user_info_)
print(f"Popped item is {popped_item}")
# print(type(popped_item))


# 3. Popitem() Method

#This method will Pop random item in your dictionary
#This method will also return the popped item 

popped_item2 = user_info_.popitem()
print(user_info_)
print(f"Popped item is {popped_item2}")
print(type(popped_item2))