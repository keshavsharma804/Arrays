# # Iterate Python Program to print alternate elements
# def aler(arr):
#     res = []
#     for i in range(0, len(arr), 2):
#         res.append(arr[i])
#     return res

# arr = [10, 20, 30, 40, 50]
# res = aler(arr)
# print(" ".join(map(str, res)))



# # Find Second Smallest and Second Largest
# def sort(arr):
#     sorted_arr = sorted(arr)
#     second_smallest = sorted_arr[1]
#     second_largest = sorted_arr[-2]
#     return second_smallest, second_largest

# arr = [15, 14, 5, 25, 44, 23]
# secnd_smallest, secnd_largest  = sort(arr)
# print("Second Smallest:", secnd_smallest)
# print("Second Largest:", secnd_largest)


# #
# def sort(arr):
#     for i in range(len(arr) -1):
#         if arr[i] >  arr[i+1]:
#             return False
#     return True
# arr = [15,14, 25, 4]
# check = sort(arr)
# print(check)




# # Left rotate the array by one
# def left_rotate(arr):
#     # Store the first element of the array
#     first_element = arr[0]
    
#     # Shift all elements one position to the left
#     for i in range(1, len(arr)):
#         arr[i - 1] = arr[i]
    
#     # Place the first element at the last position
#     arr[-1] = first_element

# arr = [4, 3, 5, 2, 1]
# left_rotate(arr)
# print("Array after left rotation by one:", arr)


# #Two Sum
# def two(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             return [i, j]
#     return [-1. -1]

# arr = [2, 7, 11, 15]
# target = 9
# print(two(arr, target))


# # sort the array without using inbuilt sort functions.
# def sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# array = [2,0,2,1,1,0]
# print("Array sorted by absolute values:", sort(array))


# # Majority Element that occurs more than N/2 times
# def cnt(arr):
#     n = len(arr)
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[j] == arr[i]:
#                 count+= 1
#         if count > (n//2):
#             return arr[i]
#     return -1

# arr = [2, 2, 1, 1, 1, 2, 2]
# ans = cnt(arr)
# print("The majority element is:", ans)


# # Move Zeros to end (CG)
# def moveZeros(a):
#     pos = 0  
    
#     for i in range(len(a)):
#         if a[i] != 0:
#             a[pos], a[i] = a[i], a[pos]  
#             pos += 1
#     return a

# arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# ans = moveZeros(arr)
# print(*ans)  

   
# def peakElement(arr):
#     n = len(arr)
#     if n == 1:
#         return "true" 

#     if arr[0] > arr[1]:
#         return "true"
#     if arr[-1] > arr[-2]:
#         return "true"

#     for i in range(1, n - 1):
#         if arr[i-1] < arr[i] > arr[i+1]:
#             return "true"    
#     return "false"

# arr = [1, 2, 4, 5, 7, 8, 3]
# value = peakElement(arr)
# print(value)  


# def search(arr, x):
#     for i in range(0, len(arr)):
#         if x == arr[i]:
#             return i
#     return -1

# arr = [1, 2, 3, 4]
# x = 3
# value = search(arr, x)
# print(value)


# # Array Subset (CG)
# def subset(a, b):
#     return all(item in b for item in a)

# a = [11, 7, 1, 13, 21, 3, 7, 3]
# b = [11, 3, 7, 1, 7]
# value = subset(a,b)
# print(value)


# # Reverse Group Array----------------------------------------------------Try Again---------------------
# def reverse_in_groups(arr, k):
#     n = len(arr)
#     for i in range(0, n, k):
#         left = i
#         right = min(i + k - 1, n - 1)
#         while left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#     return arr

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# result = reverse_in_groups(arr, k)
# print(result)  


# # Max and Min
# def max_min(arr):

#     max_value = arr[0]
#     min_value = arr[0]
    
#     for i in range(1, len(arr)):  
#         if arr[i] > max_value:
#             max_value = arr[i]
#         if arr[i] < min_value:
#             min_value = arr[i]
    
#     return max_value, min_value

# arr = [3, 2, 1, 56, 10000, 167]
# max_value, min_value = max_min(arr)
# print(max_value,min_value)


# def rotate(arr):
#     last_element = arr[-1]
#     for i in range(len(arr) - 1, 0, -1):
#         arr[i] = arr[i-1]
#     arr[0] = last_element
#     return arr

# arr = [1, 2, 3, 4, 5]
# rot = rotate(arr)
# print(rot)


# # Value equal to index value
# def valueEqualToIndex(arr):
#     result = []
#     for i in range(len(arr)):
#         if arr[i] == i+1:
#             result.append(arr[i])
#     return result

# arr = [15, 2, 45, 4 , 7]
# result = valueEqualToIndex(arr)
# print(result)

# def immediateSmaller(arr):
#     for i in range(len(arr), -1):
#         if arr[i] > arr[i+1]:
#             arr[i] = arr[i+1]
#         else:
#             arr[i] = -1
#     arr[-1] = -1
#     return arr

# arr = [4, 2, 1, 5, 3]
# value  = immediateSmaller(arr)
# print(value)
        

# #First and Second Smallest   (CG)
# def find_first_and_second_smallest(arr):
#     if len(arr) < 2:
#         return -1
    
#     first = second = float('inf')
    
#     for num in arr:
#         if num < first:
#             second = first
#             first = num
#         elif num < second and num != first:
#             second = num
    
#     if second == float('inf'):
#         return -1
    
#     return first, second


# # Replace 0 with 5
# def convertFive(n):
#     string = str(n)
#     modified = string.replace('0', '5')
#     num = int(modified)
#     return num


# # Get Odd (CG)
# def get(arr, n):
#     result = 0
#     for num in arr:
#         result ^= num
#     return result if result != 0 else -1

        
# arr = [5,7,2,7,5,2,5]
# n = 7
# num = get(arr, n)
# print(num)


# # Swap kth element (CG)
# def swapKth(self, k, arr):
#     n = len(arr)
#     # Ensure k is within the valid range
#     if k <= 0 or k > n:
#         return "Invalid k"
#     arr[k-1], arr[n-k] = arr[n-k], arr[k-1]
#     return arr


# # Elements in range
# def check_elements(arr, A, B):
#     for i in range(A, B + 1):
#         if i not in arr:
#             return False
#     return True

# arr = [1,4,5,2,7,8,3]
# A = 2
# B = 5
# val = check_elements(arr, A, B)
# print(val)



# # At least two greater elements
# def findElements(self, arr):
#         if len(arr) < 2:
#             return -1

#         greatest = second_greatest = float('-inf')

#         for num in arr:
#             if num > greatest:
#                 second_greatest = greatest
#                 greatest = num
#             elif num > second_greatest and num != greatest:
#                 second_greatest = num

#         result = [num for num in arr if num < second_greatest]
#         result.sort()
#         return result


# # Find the fine
# def totalFine(date, car, fine):
#     sum = 0
#     for i in range (len(car)):
#         if car[i]%2 != 0 and date%2 == 0:
#             sum += fine[i]
#         elif car[i]%2 == 0 and date%2 !=0:
#             sum += fine[i]
#     return sum

# date = 12
# car = [2375, 7682, 2325, 2352]
# fine = [250, 500, 350, 200]
# value = totalFine(date, car, fine)
# print(value)


# #First 1 in a Sorted Binary Array
# def first(arr):
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             return i
#     return -1

# arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
# value = first(arr)
# print(value)

       
# # Max and Min Product from 2 Arrays
# def find_multiplication(arr1, arr2):
#     max = float('-inf')
#     min = float('inf')

#     for i in arr1:
#         if i > max:
#             max = i
#     for i in arr2:
#         if i < min:
#             min = i
    
#     mul = max * min
#     return mul


# def findtriplet(arr):
#     sort = sorted(arr)
#     for i in range(0, len(sort) -1):
#         for j in range(i+1, len(sort)):
#             sum = sort[i] + sort[j]
#             if sum in sort[j+1:]: 
#                 return True
#     return False

# arr = [3,4,5]
# value = findtriplet(arr)
# print(value)


# # Max Product of two number
# def max(arr):
#     prod = float('-inf')
#     for i in range(0, len(arr) -1):
#         for j in range(i+1, len(arr)):
#             product = arr[i] * arr[j]
#             if product > prod:
#                 prod = product
#     return prod

# # Segregate Even and Odd numbers
# def seg(arr):
#     new = []
#     new2 = []
#     for i in range(0, len(arr)):
#         if arr[i]%2 == 0:
#             new.append((arr[i]))
#         else:
#             new2.append(arr[i])
#     return sorted(new) + sorted(new2)        


# arr = [12, 34, 45, 9, 8, 90, 3]
# value = seg(arr)
# print(value)
            

# def maxNtype(arr):
#         if arr == sorted(arr):
#             return 1
    
   
#         if arr == sorted(arr, reverse=True):
#             return 2

#         min_index = arr.index(min(arr))  
#         max_index = arr.index(max(arr))  
    
    
#         if min_index > 0 and max_index < min_index:
#             return 4
    
 
#         if max_index > 0 and min_index < max_index:
#             return 3


# # # Positive and negative elements
# # def arrange(arr):
# #     positive = [x for x in arr if x > 0]
# #     negative = [x for x in arr if x < 0]

# #     i, j = 0,0
# #     result = []

# #     while i < len(positive) and j < len(negative):
# #         result.append(positive[i])
# #         result.append(negative[j])

# #         i+= 1
# #         j+= 1
# #     return result


## Second Largest

# def second_largest(arr):
#     if not arr:
#         return None
#     second_largest = float('-inf')
#     largest_element = float('-inf')


#     for i in range(len(arr)):
#         if arr[i] > largest_element:
#             second_largest = largest_element
#             largest_element = arr[i]
#         elif arr[i] > second_largest and arr[i] < largest_element:
#             second_largest = arr[i]
            
#     return second_largest
        
# arr = [1, 2, 3, 4, 5]
# value = second_largest(arr)
# print(value)



# def union(a,b):
#     val = set()
#     for i in a:
#         val.add(i)
#     for j in b:
#         val.add(j)
#     return val

# def sum(arr, target):
#     val = ()
#     for i in arr:
#         val.add(i)
#     for j in arr:
#         val.add(j)
#             if i + j == target:
#                 return True

## Two Sum
# def two(arr, target):
#     for i in range(0, len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return i,j


# Remove duplicate from sorted array
def dup(arr):
    if not arr:
        return 0
    i = 0

    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i] = arr[j]
            i+=1

    return i + 1

## Remove Element 
def rem(arr,val):
    if not arr:
        return 0
    i = 0
    for j in range(0, len(arr)):
        if val != arr[j]:
            arr[i] = arr[j]
            i+=1
            
    
    return i