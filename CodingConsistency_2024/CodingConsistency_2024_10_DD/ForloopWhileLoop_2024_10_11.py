#Simple Loop code that uses While and For Loop

numbers = [3, 5, 2]

for num in numbers:
    print(f"Counting down from {num}:")
    
    while num > 0:
        print(num)
        num -= 1  
    
    print("Done!\n")
