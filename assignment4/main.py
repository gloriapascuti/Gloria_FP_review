# Consider a positive number n. Determine all its decompositions as sums of prime numbers.
# 1. make a prime function that checks when a number is prime
# 2. understand how backtracking works using an example (on another problem)
# 3. think about your problem and understand the steps that you have to take
# 4. implement decomposition function to decompose the number
# 5. check if the numbers in the function are prime
# 6. is you don't know how to implement it directly using backtracking, try implementing it as usual
# 7. make sure you understood what you did
from typing import List


def is_prime(value: int) -> bool:
    """
    This function checks if a certain number is prime
    :param value: the number to be checked
    :return: the truth depending on the value
    """
    if value <= 1:
        return False
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            return False
    return True

def next_prime(value):
    while True:
        if is_prime(value):
            return value
        value += 1


def prime_decompositions_recursive(value: int) -> List[List[int]]:
    def backtrack(current: int, target: int, partial: List[int], res: List[List[int]]):
        if target == 0:
            res.append(partial[:])

        while current <= value:
            current = next_prime(current)
            if target - current >= 0:
                partial.append(current)
                backtrack(current, target - current, partial, res)
                partial.pop()
            current += 1

    result = []
    backtrack(0, value, [], result)
    return result

def prime_decompositions_iterative(value: int) -> List[List[int]]:
    stack = [(0, value, [])]
    result = []

    while stack:
        current, target, partial = stack.pop()

        if target == 0:
            result.append(partial[:])
            continue

        while current <= value:
            current = next_prime(current)
            if target - current >= 0:
                stack.append((current, target - current, partial + [current]))
            current += 1

    return result

def prime_decompositions_recursive_duplicates(value: int) -> List[List[int]]:
    def backtrack(target: int, partial: List[int], res: List[List[int]]):
        if target == 0:
            res.append(partial[:])

        for current in range(value + 1):
            if is_prime(current) and target - current >= 0:
                partial.append(current)
                backtrack(target - current, partial, res)
                partial.pop()

    result = []
    backtrack(value, [], result)
    return result

def prime_decompositions_iterative_duplicates(value: int) -> List[List[int]]:
    stack = [(value, [])]
    result = []

    while stack:
        target, partial = stack.pop()

        if target == 0:
            result.append(partial[:])
            continue

        for current in range(value + 1):
            if is_prime(current) and target - current >= 0:
                stack.append((target - current, partial + [current]))

    return result


def main():
    print("This is the recursive decomposition:")
    print(prime_decompositions_recursive(13))
    print("\nThis is the iterative decomposition:")
    print(prime_decompositions_iterative(13))
    print("\nThis is the recursive decomposition with duplicates:")
    print(prime_decompositions_recursive_duplicates(13))
    print("\nThis is the iterative decomposition with duplicates:")
    print(prime_decompositions_iterative_duplicates(13))


if __name__ == '__main__':
    main()
