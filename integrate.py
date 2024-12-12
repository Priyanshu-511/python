import argparse
from sympy import symbols, integrate, sympify

# Define the argument parser
parser = argparse.ArgumentParser(description="Compute the integral of a given function.")
parser.add_argument("function", type=str, help="The function to integrate (e.g., 'sin(x)', 'x**2').")
parser.add_argument("--variable", type=str, default="x", help="The variable of integration (default: x).")
parser.add_argument("--lower", type=float, help="The lower limit for definite integration.")
parser.add_argument("--upper", type=float, help="The upper limit for definite integration.")

# Parse the arguments
args = parser.parse_args()

# Define the symbolic variable
variable = symbols(args.variable)

# Convert the function string to a SymPy expression
try:
    func = sympify(args.function)
except Exception as e:
    print(f"Error parsing the function: {e}")
    exit(1)

# Perform integration
if args.lower is not None and args.upper is not None:
    # Definite integral
    result = integrate(func, (variable, args.lower, args.upper))
else:
    # Indefinite integral
    result = integrate(func, variable)

# Output the result
print(f"Integral of {args.function}: {result}")



'''
in terminal
python integrate.py "x**2"
python integrate.py "x**2" --lower 0 --upper 2
python integrate.py "y**3" --variable y
'''

