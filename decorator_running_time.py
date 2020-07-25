import timeit


def time(function,*arg):
    return time


def running_time(function):
    

    def wrapper(*arg,**kwargs):
        
        start = timeit.default_timer()
        value = function(*arg) 
        end = timeit.default_timer()
        function.timetaken = end - start
        return value
    return wrapper

@running_time
def expensive_operation(one, two):
   import time
   time.sleep(one)
   time.sleep(two)
   return one + two 

if __name__ == '__main__':
     print expensive_operation(1, 2)
    