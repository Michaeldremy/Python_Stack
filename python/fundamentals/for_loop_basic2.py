arr = [-1, 3, 5, -5]
def biggie_size(arr):
    for x in range(len(arr)):
        if(arr[x]>0):
            arr[x]= "big"
    return arr
arr2 = biggie_size(arr)
print(arr2)
# output prints [-1, "big", "big", -5]
arr = [-1,1,1,1]
def count_positives(arr):
    count = 0
    for x in range(len(arr)):
        if(arr[x]>0):
            count += 1
        arr[(len(arr))-1] = count
    return arr
arr2 = count_positives(arr)
print(arr2)
# Output prints [-1,1,1,3]
arr = [1,2,3,4]
def sum_total(arr):
    sum = 0
    for x in range(len(arr)):
        sum += arr[x]
    return sum
num = sum_total(arr)
print(num)
# Output prints 10
arr = [1,2,3,4]
def average(arr):
    sum = 0
    for x in range(len(arr)):
        sum += arr[x]

    return sum / len(arr)
avg = average(arr)
print(avg)
# Output prints 2.5
arr = [37,2,1,-9]
def length(arr):
    return len(arr)
print(length(arr))
# Output prints 4
arr = [37,2,1,-9]
def minimum(arr):
    if len(arr) == 0:
        return False
    lowest = arr[0]
    for x in range(len(arr)):
        if arr[x]<lowest:
            lowest = arr[x]
    return lowest
print(minimum(arr))
print(minimum([]))
# Output prints -9 and False
arr = [37,2,1,-9]
def maximum(arr):
    if len(arr) == 0:
        return False
    greatest = arr[0]
    for x in range(len(arr)):
        if arr[x]>greatest:
            greatest = arr[x]
    return greatest
print(maximum(arr))
print(maximum([]))
# Output prints 37 and False
def ultimate_analysis(arr):
    return {"sumTotal": sum_total(arr), "average": average(arr), 'minimum': minimum(arr), 'maximum': maximum(arr), 'length': length(arr)}
print(ultimate_analysis(arr))
# ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
arr = [37,2,1,-9]
def reverse_list(arr):
    arr_MidIndex = len(arr) // 2
    for x in range(arr_MidIndex):
        temp = arr[x]
        arr[x] = arr[len(arr)-1-x]
        arr[len(arr)-1-x] = temp
    return arr
print(reverse_list(arr))
# Output prints [-9,1,2,37]
