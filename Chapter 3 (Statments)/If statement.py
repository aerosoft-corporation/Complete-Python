# # Game
# age = int(input("Enter your age: "))
# if age >= 14:
#     print("You can play")
# else:
#     print("you cannot play")
#     pass
# # Weather
# temp = int(input("Enter Temperature: "))
# if temp >= 25:
#     print("weather is hot")
# else:
#     print("weather is cold")
#     pass
# Exercise
Winning_Number = 50
User_input = int(input("Guess The Correct Nmuber And Win The Game: "))
if User_input == Winning_Number:
    print ("YOU WON...!!!")
else:    #Nested IF ELSE statement>>>>
    if User_input > Winning_Number:
        print("TOO HIGH")
    else:
        print("TOO LOW")