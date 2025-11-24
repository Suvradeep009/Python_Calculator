PYTHON CLI CALCULATOR & MATRIX TOOL

OVERVIEW This project is a command-line interface (CLI) scientific calculator built in Python. It bridges the gap between standard scalar arithmetic and more advanced mathematical operations, specifically Trigonometry and Linear Algebra (Matrix operations).

The application is designed with a modular structure, processing inputs via a main event loop and delegating logic to specialized handlers. It relies solely on the Python standard library (math), requiring no external dependencies.

FEATURES

Stateful Arithmetic: Performs basic operations (+, -, *, /) and caches results for chained calculations.

Advanced Trigonometry: Evaluates complex trigonometric expressions (e.g., "sin(30) + cos(60)") using degrees. Includes safety handling for undefined values.

Matrix Operations: Supports Matrix Addition and Matrix Multiplication with dimension validation.

SETUP AND INSTALLATION

Prerequisites:

Python 3.6+ is required.

No external packages (pip install) are needed.

Installation:

Save the provided code into a file named calculator.py.

Open your terminal or command prompt.

Navigate to the directory containing the file.

Execution: Run the script using the standard Python interpreter: python calculator.py

USAGE GUIDE

Basic Arithmetic Standard operations are supported. If a previous result exists, the system will ask if you wish to use it as the first operand for the next calculation.

Trigonometry Input expressions using standard function names.

Input Format: Functions take arguments in Degrees.

Supported Functions: sin, cos, tan, sec, csc, cot, sqrt, pi, abs.

Example: Enter expression: tan(45) + sin(30) Result: 1.5000

Matrix Operations The tool supports addition and multiplication. Input is handled row-by-row.

Input Format: Enter all numbers for a specific row separated by spaces.

Example (2x2 Identity Matrix): Row 1: 1 0 Row 2: 0 1

TECHNICAL IMPLEMENTATION DETAILS

A. Arithmetic & State Management The main() function operates an infinite while loop. The state is maintained via the current_result variable. When perform_arithmetic is called, it checks if current_result is not None and prompts the user to reuse it, effectively acting as the "Ans" key on physical calculators.

B. Trigonometric Evaluation Engine The trigonometry module uses Python's eval() function, but it is sandboxed for security and convenience.

Environment Restriction: eval is restricted to a specific dictionary (trig_env) containing only math functions and constants. builtins is set to None to prevent code injection.

Degree Conversion: Python's math module expects radians. Wrapper functions (e.g., safe_sin) automatically convert user input x from degrees to radians: radians = x * pi / 180.

Singularity Handling: Functions like tan(x) or sec(x) are undefined at certain angles (e.g., 90 degrees). The code implements epsilon-based checks to handle floating-point inaccuracies and singularities. For example, if abs(cos(x)) < 1e-10, the system raises a ValueError("Undefined").

C. Matrix Logic Matrices are represented as Lists of Lists ([[row1], [row2]]).

Matrix Addition: Performs element-wise addition. Requires Matrix A and Matrix B to have identical dimensions m x n. Formula: C[i][j] = A[i][j] + B[i][j]

Matrix Multiplication: Performs the dot product of rows and columns. Requires specific dimensions: If A is m x n and B is n x p, the result C is m x p. The implementation uses a standard O(n^3) nested loop approach: Formula: C[i][j] = sum(A[i][k] * B[k][j])

ERROR HANDLING

Zero Division: Caught in arithmetic mode to prevent crashes.

Input Validation: try-except blocks ensure non-numeric input does not terminate the program during matrix entry.

Dimension Mismatch: Explicit checks prevent invalid matrix operations before processing begins.
