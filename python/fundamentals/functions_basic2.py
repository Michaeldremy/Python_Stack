def countdown(num):
    for x in range(num,0,-1):
        print (x)
# output example countdown 5 would return [5,4,3,2,1,0]
def print_and_return(arr):
    print(arr[0])
    return arr[1]
# output example def print_and_return([1,2]): will print 1 and return 2.
def greater(arr):
    sub_arr = []
    if len(arr) == 0:
        return False
    for x in arr:
        if arr[x] > arr[1]:
            sub_arr.append(arr[x])
    print(sub_arr)
    print(len(sub_arr))
# output example greater([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# output example greater([3]) should return False
def length_and_value(num1,num2):
    sub_arr = []
    if num1 == num2:
        print("Jinx")
    for x in range (0, num1):
        sub_arr.append(num2)
    return sub_arr
# output example length_and_value(4,7) should return [7,7,7,7]
# output example length_and_value(6,2) should return [2,2,2,2,2,2]
