def fibonacci_non_recursive(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 3
print(f"Fibonacci number at position {n} (recursive): {fibonacci_recursive(n)}")
print(f"Fibonacci number at position {n} (non-recursive): {fibonacci_non_recursive(n)}")
