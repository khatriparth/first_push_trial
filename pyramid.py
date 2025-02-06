def print_pyramid(n):
    for x in range(1, n + 1):
        for y in range(n - x):
            print(" ", end="")

        for k in range(1, 2 * x):
            print("*", end="")
        print()


print_pyramid(10)