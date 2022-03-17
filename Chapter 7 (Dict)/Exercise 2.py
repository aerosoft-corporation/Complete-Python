# Exercise No 2. 

# user_info_1 = {
#     'name' : 'Abbas',
#     'age' : 21,
#     'fav_movies' : ['The Martian', 'Rio'],
#     'fav_Songs' : ['Edward Maya', 'Akcent']
# }

# Statement 
# Take input from users and print dictionary in this order ^

# Solution 
user = {}
name = input('Enter Your Name : ')
age = input('Enter Your Age : ')
fav_movie = input('Enter Your Fav_Movies (Comma Separated \',\') : ').split(',')
fav_songs = input('Enter Your Fav_Songs (Comma Separated \',\') : ').split(',')

user['name'] = name
user['age'] = age
user['fav_movie'] = fav_movie
user['fav_songs'] = fav_songs

# print(user)

for key, value in user.items():
    print(f"{key} : {value}")




# Method 2 using def() function
def order(name, age, fav_movie, fav_songs):
    user = {}
    user['name'] = name
    user['age'] = age
    user['fav_movie'] = fav_movie
    user['fav_songs'] = fav_songs
    for key, value in user.items():
        print(f"{key} : {value}")
    # return user

name = input('Enter Your Name : ')
age = input('Enter Your Age : ')
fav_movie = input('Enter Your Fav_Movies (Comma Separated \',\') : ').split(',')
fav_songs = input('Enter Your Fav_Songs (Comma Separated \',\') : ').split(',')
order(name, age, fav_movie, fav_songs)