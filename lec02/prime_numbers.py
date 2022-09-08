def is_prime_number(n):
    # n == 5 => True
    # n == 6 => False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    # 100 <= n < 200에서, prime number와 갯수
    # count = 0
    prime_numbers = []
    for n in range(100, 200):
        if is_prime_number(n):
            # print(n)
            # count += 1
            prime_numbers.append(n)
    print(len(prime_numbers))
    print(prime_numbers)


if __name__ == "__main__":
    main()
