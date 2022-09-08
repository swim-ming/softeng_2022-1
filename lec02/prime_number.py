def is_prime_number(n):
    # n == 5 => True
    # n == 6 => False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    n = 5
    print("{} => {}".format(n, is_prime_number(n)))


if __name__ == "__main__":
    main()
