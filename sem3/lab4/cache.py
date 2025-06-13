import time
from functools import cache

def fibDict(n, dictionary = None):
    if dictionary is None:
        dictionary = {}
    if n in dictionary:
        return dictionary[n]
    if n in (1, 2):
        return 1
    dictionary[n] = fibDict(n - 1, dictionary) + fibDict(n - 2, dictionary)
    return dictionary[n]

@cache
def fibCache(n):
    if n in (1, 2):
        return 1
    return fibCache(n - 1) + fibCache(n - 2)

start_time = time.time()
gg = fibDict(100)
end_time = time.time()
print(gg, end_time - start_time)