# Problem-4: Count how many numbers in the list are divisible by 1 through 9
# Input: list of integers
# Output: dictionary {1: count, 2: count, ..., 9: count}

def count_multiples(numbers):
    result = {i: 0 for i in range(1, 10)}
    
    for num in numbers:
        for divisor in range(1, 10):
            if num % divisor == 0:
                result[divisor] += 1
                
    return result

# Test
if __name__ == "__main__":
    input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    output = count_multiples(input_list)
    print(output)