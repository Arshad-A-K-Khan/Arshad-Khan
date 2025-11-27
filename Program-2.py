# Problem-2: Print first n odd numbers
# Input: integer x
# Output: 1, 3, 5, 7, ... up to x terms

def print_odd_numbers(x):
    if x <= 0:
        print("Please enter a positive integer")
        return
    
    result = []
    for i in range(1, 2*x, 2):  # Start from 1, step by 2, up to (2*x-1)
        result.append(i)
    
    print(", ".join(map(str, result)))

# Test cases
if __name__ == "__main__":
    print("Input: 1")
    print_odd_numbers(1)
    print("\nInput: 2")
    print_odd_numbers(2)
    print("\nInput: 3")
    print_odd_numbers(3)
    print("\nInput: 4")
    print_odd_numbers(4)