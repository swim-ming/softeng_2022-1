
def k2c(k):
    return k - 273.15


def mi2km(mi):
    return mi * 1.6


def main():
    k = 285.3
    mile = 300

    print("{:.1f}K => {:.1f}C".format(k, k2c(k)))
    print("{:.1f}mi. => {:.1f}km".format(mile, mi2km(mile)))


if __name__ == "__main__":
    main()
