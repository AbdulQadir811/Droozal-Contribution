import bubble_sort
def reverse(some_function):


    def wrapper(*arg, **kwarg):
      
      result =  some_function(*arg)
      return result[::-1] 
    return wrapper

@reverse
def bubble_sort(list1):
    swapped = 0
    for i in range(0, len(list1)):
        for j in range(0, len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                swapped = 1
            if swapped == 0:
                return list1
    return list1

arr = [1, 3, 2, 5, 7]
print bubble_sort(arr)
