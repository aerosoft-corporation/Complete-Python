# Common Element finder function
# Define a function which take 2 lists as input and return a list which contains common elements of both list

# Example 
# input ----> [1,2,5,8], [1,2,7,6]
# Output ----> [1,2]

def common_finder(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

l1 = [1,2,3,4,5,6,7]
l2 = [1,3,5,7,10,12]
total = common_finder(l1, l2)
print(f"Common Numbers Are {total}")