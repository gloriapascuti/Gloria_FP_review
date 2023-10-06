print("")
def first_prime_number(number):
    def is_not_prime(number):
        flag = False
        for i in range(2, number):
            if number % i == 0:
                flag = True
        return flag

    while  is_not_prime(number):
        number = number + 1
    return number

number = int(input("Enter a number: "))
print("Problem 1: ")
print(first_prime_number(number))
print("")

# Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n.
# Two prime numbers p and q are called twin if q - p = 2.

def twin_prime(number):
    first = first_prime_number(number)
    second = first_prime_number(first+1)
    while second - first != 2:
        first = second
        second = first_prime_number(second+1)
    if second - first == 2:
        print((first, second))
        return True
print("Problem 2:")
twin_prime(number)
print("")

# print("This program is designed to give the use the largest perfect number, smaller than the number given.")
# number = int(input("So come on and enter a number: "))

def largest_perfect_number(number):
    def sum_divisors(number):
        sum = 1
        for i in range(2, number - 1):
            if number % i == 0:
                sum += i
        return sum
    number -= 1
    while sum_divisors(number) != number and number != 0:
        number -= 1
    if number == 0 or number == 1:
        print("Error. Unfortunately such number does not exist.")
#        number = int(input("Enter a new number: "))
#        largest_perfect_number(number)
    else:
        print(number)

print("Problem 3:")
largest_perfect_number(number)
