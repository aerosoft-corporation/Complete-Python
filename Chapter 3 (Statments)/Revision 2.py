winning_number = 55
guess = 1
user_input = int(input("Enter a Number b/w 1 and 100: "))
game_over = False
while not game_over:
    if user_input == winning_number:
        print (f"YOU WON !!! And you Tried it {guess} time : ")
        game_over = True
    else:
        if user_input > winning_number:
            print ("TOO HIGH!!!")
            guess += 1
            user_input = int(input("Guess Again: "))
        else:
            print ("TOO LOW!!!")
            guess += 1
            user_input = int(input("Guess Again: "))
            pass
