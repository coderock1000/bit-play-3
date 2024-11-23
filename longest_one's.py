def longest_ones(num):
    longest = 0
    current = 0

    while num > 0:
        if num & 1: 
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0
        num >>= 1  
    return longest

number = int(input("Enter a number: "))
print("The longest 1's in the binary representation is:", longest_ones(number))
