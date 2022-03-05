# # AND OPERATOR:
name = "Abbas"
age = 21
if name=="Abbas" and age==21:
    print("Condition Is True")
else:
    print("Condition Is False")
    pass
# # If one condition is false then AND operator will make all the condition is false
#
#
# # OR OPERATOR
if name=="abbas" or age=="21":
    print("Condition is true ")
else:
    print("Condition is False")
    pass
# if one condition is false the OR operator make all the condition are true if the
# all condition are false then OR operator will make condiotion false
# Exercise
user_name = input("Enter Your Name: ")
user_age = int(input("Enter Your Age: "))
if user_age >= 10 and (user_name[0]=="a" or user_name[0]=="A"):
    print("You Can Watch Coco")
else:
    print("You Cannot Watch Coco")
    pass