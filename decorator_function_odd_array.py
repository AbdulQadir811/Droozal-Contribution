def odd_number_array(some_function):


    def wrapper(*arr):
        arr_2 = []
        arr_1 = some_function(*arr)
        for i in range(len(arr_1)):
           if arr_1[i] % 2 != 0 :
                arr_2.append(arr_1[i])   
        return some_function(arr_2)

    return wrapper

@odd_number_array
def just_some_function(arr):    
    return arr


if __name__ == '__main__':
    arr =[1, 2, 3, 4]
    print just_some_function(arr)
