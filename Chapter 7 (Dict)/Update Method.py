user_info_1 = {
    'name' : 'Abbas',
    'age' : 21,
    'fav_movies' : ['The Martian', 'Rio'],
    'fav_Singer' : ['Edward Maya', 'Akcent']
}

# If you update the name again. The new name will be print() instead of previous name.
new_info = {'father name' : 'Fazal Karim Fazal', 'Address' : 'Shinkiari', 'name' : 'Abbas Ali'}
user_info_1.update(new_info)
print(user_info_1)