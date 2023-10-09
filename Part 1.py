#File: part1.py
#Author: Taha Aktan
#Date: 10/8/2023
#Description: Extended Ecluid's algorithm



def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_euclidean(b, a % b)
    
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y


m = 45  
n = 40
d, x, y = extended_euclidean(m, n)

print(f"GCD({m}, {n}) = {d}")
print(f"x = {x}, y = {y}")
print(f"{m}*{x} + {n}*{y} = {d}")

