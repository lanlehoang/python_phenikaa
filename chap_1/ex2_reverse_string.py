def reverse_string(s):
    return s[::-1]


if __name__ == "__main__":
    s = input().strip()
    print(reverse_string(s))