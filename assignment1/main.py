number = int(input("Enter a number: "))
def is_not_prime(variable):
    identical = variable
    flag = False
    for i in range(2, identical):
       if number % i == 0:
            flag = True
    return flag

while  is_not_prime(number):
    number = number + 1

print(number)