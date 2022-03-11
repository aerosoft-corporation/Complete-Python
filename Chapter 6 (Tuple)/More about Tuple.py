# 1. Looping In Tuples
item = (1, 2, 3, 'four', 'five', 6.0, None)
# For Loop
for i in item:
    print(i)

# While Loop
i = 0
while i < len(item):
    print(item[i])
    i += 1

# 2. Tuple with One element
tpl = (1)    #Not Tuple this is int Var
print(type(tpl))
tpl2 = ('Word')    #Not Tuple this is String Var
print(type(tpl2))

# NOTE - Tuple with One element, we require comma for declare as tuple
tpl3 = (1,)    #This is tuple 
print(type(tpl3))
tpl4 = ('word',)
print(type(tpl4))

# 3. Tuple without paranthesis
extpl = 1,2,3,4    #There is no matter that use paranthesis or not. No Error
print(extpl)

# 4. Tuple unpacking 
cricketer = ('Afridi', 'Inzimam', 'UmarAkmal')
crk1, crck2, crck3 = cricketer
print(crk1)

# 5. List inside Tuple
fav = ('Afirdi', ['Inzimam', 'Abdurrazaq'])
fav[1][0] = 'Umar'
fav[1].pop()
fav[1].append('Kamran')

print(fav)


# Some function that you can use in tuple
# max(), min(), sum(), len()
num = (1, 2, 3, 4)
print(max(num))
print(min(num))
print(sum(num))
print(len(num))
