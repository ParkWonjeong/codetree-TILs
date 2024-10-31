n = int(input())
def print_n(n):
    if n == 0:
        return

    print_n(n - 1)
    print("HelloWorld")

print_n(n)