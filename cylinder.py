import math
import stdio
import sys

# Gets the input from the terminal and stores in into the variables
r = float(sys.argv[1])
h = float(sys.argv[2])

# Equation that gets the surface area of the dimensions of the square
S = math.pi * 2 * r * (r + h)
# Equation that gets the volume of the dimensions of the square
V = math.pi * r**2 * h

# displays the surface area and volume of the square
stdio.writeln("S = " + str(S))
stdio.writeln("V = " + str(V))
