#Fibonacci Sequence
n_terms = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a, end=" ")
        # Update values
        a, b = b, a + b
        count += 1
