####################################################
##  COUNT PRIMES: Write a function that returns the number of prime numbers that exist 
#   up to and including a given number
#   count_primes(100) --> 25
#   By convention, 0 and 1 are not prime.
####################################################
'''
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

'''
#####################################################
'''
num = 13
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(f"{i} is not a prime number")
            break
        else:
            print(f"{i} is a prime number")
else:

    print(f"{i} is not a prime number")

'''

########################################################
########################################################
# Program to check if a number is prime or not
# Input from the user
num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
    # Check if factor exist

    for i in range(2,num):
        print(f"Checking  {i}")
        if (num % i) == 0:
            print(num,"is not a prime number")
        #    break
    else:
        print(num,"is a prime number")

# Else if the input number is less than or equal to 1
else:
    print(num,"is not a prime number")

#########################################################
#########################################################