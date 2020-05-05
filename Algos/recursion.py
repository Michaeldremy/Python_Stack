# Recursion is just a function that calls itself

# Example: 
# def Print1ToNum(num):
#     if num == 1:
#         print(1)
#         return
#     Print1ToNum(num - 1)    
#     print(num)
#     return

# Print1ToNum(10)

    # write a sigma function using recursion, where Sigma(num) will return the sum of the
    # numbers between 1 and that number (including that number)

def Sigma(num):
    sum = 0
    if num == 1:
        sum = 1
        return sum
    sum += Sigma(num - 1) + num
    return sum


print(Sigma(4))