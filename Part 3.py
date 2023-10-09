#File: part3.py
#Author: Taha Aktan
#Date: 10/8/2023
#Description: computing gcd(m, n)

def middle_school_gcd(m, n):
    while n != 0:
        remainder = m % n
        m = n
        n = remainder
    return m

# Test the function
m = 56
n = 98
print(middle_school_gcd(m, n))
