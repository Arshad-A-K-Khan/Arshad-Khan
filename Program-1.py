# Problem-1: Simple Calculator using Class
# Inputs: a (float), b (float), operation (string: "add", "subtract", "multiply", "divide")

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b == 0:
            return "Error: Division by zero!"
        return self.a / self.b

# Example usage (you can remove or comment this out)
if __name__ == "__main__":
    a = float(input('Enter the num1 : '))
    b = float(input('Enter the num2 : '))
    calc = Calculator(a, b)
    
    print(f"Addition: {calc.add()}")
    print(f"Subtraction: {calc.subtract()}")
    print(f"Multiplication: {calc.multiply()}")
    print(f"Division: {calc.divide()}")