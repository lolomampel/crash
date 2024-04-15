#value = int(input("inserte numero:"))

#if value % 2 != 0:
 #   print("Es primo")
#else:
 #   print("No es primo")

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Getting user input
num = int(input("Enter a number: "))

# Checking if the number is prime
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")