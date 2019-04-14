#!/bin/python3

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
n = int(input())

if n % 2:
    print('Weird')
elif 6 <= n <= 20:
    print('Weird')
elif (2 <= n <= 5) or n > 20:
    print("Not Weird")
