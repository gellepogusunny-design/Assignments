# decorators.py
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer
def compute(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(compute(1000000))
