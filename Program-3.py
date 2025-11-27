# Problem-3: Print odd numbers up to (2 * ceil(x/2))
# For odd n → print first n odd numbers
# For even n → print first (n-1) odd numbers
# Examples: 1→1, 2→1, 3→1,3,5, 4→1,3,5, 5→1,3,5,7,9

def print_odd_numbers_up_to_x(x):
    if x <= 0:
        print("Please enter a positive integer")
        return
    
    # Number of odd numbers to print: x if x odd, x-1 if x even
    count = (x + 1) // 2
    
    result = []
    for i in range(1, 2*count, 2):
        result.append(i)
    
    print(", ".join(map(str, result)))

# Test cases
if __name__ == "__main__":
    for n in range(1, 7):
        print(f"Input: {n}")
        print_odd_numbers_up_to_x(n)
        print()