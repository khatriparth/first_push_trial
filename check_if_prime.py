num = int(input("Enter a whole number to check if its a prime number: "))
factors = []

if num== 0 or num == 1:
    print("Special case: neither prime nor composite.")
else:
    for x in range (1, num + 1):
        y = num % x
        if y == 0:
            factors.append(x)
    if len(factors) <=2 :
        print("The number you entered is prime")
    else:
        print("The number you entered is composite")