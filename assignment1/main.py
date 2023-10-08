def is_prime(value: int) -> bool:
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def first_prime_number_greater_than(value: int) -> int:
    value += 1
    while not is_prime(value):
        value = value + 1
    return value


def twin_prime(value: int) -> None:
    first = first_prime_number_greater_than(value)
    second = first_prime_number_greater_than(first)
    while second - first != 2:
        first, second = second, first_prime_number_greater_than(first)
    print((first, second))


def sum_divisors(value: int) -> int:
    sum = 0
    for i in range(1, value):
        if value % i == 0:
            sum += i
    return sum


def largest_perfect_number_smaller_than(value: int) -> None:
    if value < 2:
        print("Error. Unfortunately such number does not exist.")
        return
    value -= 1
    while sum_divisors(value) != value and value > 1:
        value -= 1
    if value == 1:
        print("Error. Unfortunately such number does not exist.")
    else:
        print(value)


if __name__ == "__main__":
    while True:
        problem = input("Which problem do you want to run?(1/2/3 or x, if you want to exit)")
        if problem == 'x':
            break

        number = int(input("Enter a number: "))

        if problem == '1':
            print("Problem 1: ")
            print(first_prime_number_greater_than(number))
        elif problem == '2':
            print("Problem 2:")
            twin_prime(number)
        elif problem == '3':
            print("Problem 3:")
            largest_perfect_number_smaller_than(number)
        else:
            print("Error. You can only choose between 1/2/3. Please try again: ")
