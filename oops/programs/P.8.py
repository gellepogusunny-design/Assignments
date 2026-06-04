# generator.py
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(7):
    print(num)  # 0 1 1 2 3 5 8
