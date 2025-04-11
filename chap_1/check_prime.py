import math


def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))):
        if num%i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input().strip())
    print(check_prime(num))