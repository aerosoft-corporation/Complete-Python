# Dictionaries Intro
# Question - Why we use Dictionaries
# Answer - Because of limitation of list, List bare not enough to represent real data

# Example 
user = ['Abbas', 22, ['Martians', 'Sargodhyan'], ['Burak Balkan', 'Music']]

# This list cointain User Name, Age, Fav movie, fav tunes
# You can do this but this is not a good way to represent the data


# Question - What are Dictionaries
# Answer - Unordered collection of data in key : value pair
# Syntax -  {Key : Value Pair}

# Create Dictionaries
user = {"name" : "Abbas", "age" : 21}
print(user)
print(type(user))

# Second Method to create Dictionry
user1 = dict(name = 'Abbas', age = 22)
print(user1)


# Acces data from dict
# NOTE - There isn no indexing because unordered collection of data
user3 = {"name" : "Abbas", "age" : 21}
print(user3['name'])
print(user3['age'])

# Question -Which type of data can we store in dict
# Answer - Anything(int, float, String, List, Dict, Tuple etc)

user_info = {
    'name' : 'abbas',
    'age' : 21,
    'fav_movie' : ['Martians', 'Sargoshyan'],
    'fave_Tune' : ['Burak Balkan', 'Music'],
}
print(user_info['fav_movie'])

# Dict inside Dict

multi_user = {
    user1 : {
        'name' : "Abbas",
        'age' : 21,
        'address' : "Shinkiari",
        'country' : "Pakistan",
    },
    
    user2 : {
        'name' : 'Bilal',
        'age' : 19,
        'address' : "Shinkairi",
        'country' : "Pakistan",
    }
}

print(multi_user)

# How to add/remove data in dict
user4 = {}
user4['name'] = 'abbas'
user4['Age'] = 21
print(user4)







# My code Optional
test = 'Abbas'
for i in range(len(test)):
    print(*test[:i+1])