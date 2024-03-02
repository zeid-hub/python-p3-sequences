#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    a,b = 0,1
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b=b, a+b
    print(f"[{', '.join(map(str, fibonacci_sequence))}]")
print_fibonacci(9)    