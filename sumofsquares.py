import stdio

total = 0

# loops until the standard input is not empty
while not stdio.isEmpty():
    # reads the input from the terminal and stores it into the variable
    x = stdio.readInt()
    # squares each of the numbers and adds them to total
    total += x ** 2

stdio.writeln(total)
