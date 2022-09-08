def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)


def main():
    n = 5
    print("{}! => {}".format(n, factorial(n)))


if __name__ == "__main__":
    main()
