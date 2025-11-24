import math

def main():

    print("Python Calculator ")
    current_result = None
    
    while True:
        choice = get_main_menu_choice()
        
        if choice == '1':
            current_result = perform_arithmetic(current_result)
        elif choice == '2':
            current_result = perform_trigonometry(current_result)
        elif choice == '3':
        
            perform_matrix_operations() 
        elif choice == '4':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        print("\n")


def get_main_menu_choice():
    print("1. Basic Arithmetic (+, -, *, /)")
    print("2. Trigonometry (sin, cos, sec, etc. with Arithmetic)")
    print("3. Matrix Operations (Sum, Multiply)")
    print("4. Exit")
    return input("Select operation (1-4): ")

def perform_arithmetic(prev_result):
    """Handles basic scalar math."""
    num1 = get_operand(prev_result)
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return prev_result
        result = num1 / num2
    else:
        print("Invalid operator.")
        return prev_result
    
    print(f"Result: {result}")
    return result

def perform_trigonometry(prev_result):

    print("Trigonometric Mode ")
    print("Supported functions: sin(x), cos(x), tan(x), sec(x), csc(x), cot(x)")
    print("Note: 'x' must be in DEGREES.")
    print("You can combine them, e.g., 'sin(30) + sec(60)'")
    
    if prev_result is not None:
        print(f"(You can use 'ans' to refer to previous result: {prev_result})")

    expr = input("Enter expression: ")

    def safe_sin(x):
        val = math.sin(math.radians(x))
        return 0.0 if abs(val) < 1e-10 else val

    def safe_cos(x):
        val = math.cos(math.radians(x))
        return 0.0 if abs(val) < 1e-10 else val

    def safe_tan(x):
        c = safe_cos(x)
        if abs(c) < 1e-10:
            raise ValueError("Undefined")
        return math.tan(math.radians(x))

    def safe_sec(x):
        c = safe_cos(x)
        if abs(c) < 1e-10:
            raise ValueError("Undefined")
        return 1.0 / math.cos(math.radians(x))

    def safe_csc(x):
        s = safe_sin(x)
        if abs(s) < 1e-10:
            raise ValueError("Undefined")
        return 1.0 / math.sin(math.radians(x))

    def safe_cot(x):
        s = safe_sin(x)
        if abs(s) < 1e-10:
            raise ValueError("Undefined")
        return 1.0 / math.tan(math.radians(x))

    trig_env = {
        'sin': safe_sin,
        'cos': safe_cos,
        'tan': safe_tan,
        'sec': safe_sec,
        'csc': safe_csc,
        'cot': safe_cot,
        'ans': prev_result if prev_result is not None else 0,
        'pi': math.pi,
        'sqrt': math.sqrt,
        'abs': abs
    }

    try:

        result = eval(expr, {"__builtins__": None}, trig_env)
        print(f"Result: {result:.4f}")
        return result
    except ValueError as ve:

        print(f"Result: {ve}")
        return prev_result
    except Exception as e:
        print(f"Error calculating expression: {e}")
        return prev_result

def perform_matrix_operations():
    
    print("Matrix Mode: 1. Addition  2. Multiplication")
    choice = input("Choice: ")
    
    print("Matrix A Input")
    rows_a = int(input("Rows for A: "))
    cols_a = int(input("Cols for A: "))
    matrix_a = get_matrix_input(rows_a, cols_a)
    
    print("Matrix B Input ")
    rows_b = int(input("Rows for B: "))
    cols_b = int(input("Cols for B: "))
    matrix_b = get_matrix_input(rows_b, cols_b)
    
    if choice == '1':
        if rows_a != rows_b or cols_a != cols_b:
            print("Error: Dimensions must match for addition.")
            return
        result = matrix_add(matrix_a, matrix_b)
        print_matrix(result)
        
    elif choice == '2':
        if cols_a != rows_b:
            print("Error: Cols of A must equal Rows of B for multiplication.")
            return
        result = matrix_multiply(matrix_a, matrix_b)
        print_matrix(result)


def get_operand(prev_result, prompt="Enter first number: "):

    if prev_result is not None:
        use_prev = input(f"Use previous result ({prev_result})? (y/n): ").lower()
        if use_prev == 'y':
            return prev_result
    
    return float(input(prompt))

def get_matrix_input(rows, cols):
 
    matrix = []
    print(f"Enter {cols} numbers separated by space for each row:")
    for i in range(rows):
        while True:
            try:
                row_str = input(f"Row {i+1}: ")
                row = [float(x) for x in row_str.split()]
                if len(row) != cols:
                    print(f"Error: Please enter exactly {cols} numbers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers.")
    return matrix

def matrix_add(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        row_res = []
        for j in range(cols):
            row_res.append(A[i][j] + B[i][j])
        result.append(row_res)
    return result

def matrix_multiply(A, B):
    rows_a = len(A)
    cols_a = len(A[0])
    cols_b = len(B[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(M):
    print("Matrix Result:")
    for row in M:
        print(row)

# Entry Point
if __name__ == "__main__":
    main()
    
