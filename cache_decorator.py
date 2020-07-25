import random
class Cache(object):
    def __init__(self, function, max_size):
        self.function = function
        self.max_size = max_size
        self.misses = 0
        self.hits = 0
        self.size = 0
        self.my_dictionary = {}

    def __call__(self, *args, **kwargs):
        key = (self.function.__name__, args)
        if (key in self.my_dictionary.keys() or
        self.function.__name__ in self.my_dictionary and arg == 'None'):
            self.hits += 1
            return self.my_dictionary[key]
        else:
            self.misses += 1
            result = self.function(*args, **kwargs)
            self.my_dictionary[key] = result
            self.size = len(self.my_dictionary)
            if (self.size > self.max_size):
                self.size -= 1
                sum1 = self.my_dictionary[key]
                key = random.choice(self.my_dictionary.keys())
                del self.my_dictionary[key]
                return sum1
        return self.my_dictionary[key]

def cache_dumb(max_size):
    def _cache(function):
        return Cache(function,max_size)
    return _cache


@cache_dumb(5)
def calculate_sum(*args):
    import time
    time.sleep(1)
    return sum(args)

assert calculate_sum(1, 2) == 3
assert calculate_sum.size == 1
assert calculate_sum.hits == 0
assert calculate_sum.misses == 1

assert calculate_sum(1, 2) == 3
assert calculate_sum.size == 1
assert calculate_sum.hits == 1
assert calculate_sum.misses == 1

assert calculate_sum(1, 4) == 5
assert calculate_sum.size == 2
assert calculate_sum.hits == 1
assert calculate_sum.misses == 2

assert calculate_sum(1, 5) == 6
assert calculate_sum.size == 3
assert calculate_sum.hits == 1
assert calculate_sum.misses == 3

assert calculate_sum(1, 6) == 7
assert calculate_sum.size == 4
assert calculate_sum.hits == 1
assert calculate_sum.misses == 4

assert calculate_sum(1, 7) == 8
assert calculate_sum.size == 5
assert calculate_sum.hits == 1
assert calculate_sum.misses == 5

assert calculate_sum(1, 8) == 9
assert calculate_sum.size == 5
assert calculate_sum.hits == 1
assert calculate_sum.misses == 6
