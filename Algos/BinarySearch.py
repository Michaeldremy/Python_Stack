#The goal: Return a True or False boolean if the number is or not in the array.
def BinarySearch(arr, num):
    start = 0 
    end = len(arr)-1
    middle = (start+end)//2
    found = False
    while found == False:
        if num == arr[middle]:
            return True
        elif num > arr[middle]:
            start = middle + 1
            middle = (start + end)//2
        elif num < arr[middle]:
            end = middle - 1
            middle = (start + end)//2
        if start == end and arr[start] != num:
            return False
print (BinarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,100000000000000000], 5))
