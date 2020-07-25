import timeit


def fun(input_array):
    sum = 1 + 2 


def profile(function, input_array, iterations):
    time = 0
    for i in range(iterations):
    	start = timeit.default_timer()
        function(input_array)
        stop = timeit.default_timer()
        time += stop - start
    return time


if __name__ == '__main__':
    input_array = [1, 4, 5]
    print profile(fun, input_array, 1000)
