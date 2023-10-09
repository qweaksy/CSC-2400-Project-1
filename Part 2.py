#File: part2.py
#Author: Taha Aktan
#Date: 10/8/2023
#Description: Consecutive integer checking algorithm

def gcd_consecutive(m, n):
    
    gcd = 1
    
    
    divisor = max(m, n)
    
    
    while divisor > 0:
        if m % divisor == 0 and n % divisor == 0:
            gcd = divisor
            
        divisor -= 1
    
    return gcd

m = 40
n = 10
result = gcd_consecutive(m, n)
print(f"GCD of {m} and {n} is {result}")
