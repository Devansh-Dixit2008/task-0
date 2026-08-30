"""
Q3. Prime Numbers Using for-else
"""


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        # The `else` block of a for-loop runs ONLY when the loop completes
        # normally, i.e. it iterates through every value WITHOUT hitting a
        # `break`. Here, that means we never found a divisor of n, so n
        # must be prime.
        return True

    return False


def main():
    print(is_prime(7))
    print(is_prime(12))

    n = int(input("Enter N: "))
    primes = [str(num) for num in range(2, n + 1) if is_prime(num)]
    print(" ".join(primes))


if __name__ == "__main__":
    main()
