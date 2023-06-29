import subprocess

# Ask the user for the filename
filename = input("Enter the filename (without extension): ")

# Add the file extension
input_file = filename + "in.txt"
prog = filename + ".py"

# Ask the user if they want to enter the inputs themselves
choice = input("Do you want to enter the inputs yourself? (y/n): ")

if choice.lower() == "y":
    # User wants to enter the inputs
    print("Enter the inputs (press Enter twice to finish):")
    inputs = ""
    line = input()
    while line != "":
        inputs += line + "\n"
        line = input()

    # Write the inputs to the text file
    with open(input_file, 'w') as file:
        file.write(inputs)
else:
    # Read the contents of the text file
    with open(input_file, 'r') as file:
        lines = file.readlines()

# Initialize variables
tests = []
test = []
for line in lines:
    line = line.strip()
    if line == "-":
        tests.append(test)
        test = []
    else:
        test.append(line)

# Invoke the second Python program for each test
for test in tests:
    inputs = '\n'.join(test)
    print(inputs)

    # Invoke the second Python program with the inputs
    process = subprocess.Popen(['python', prog], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output = process.communicate(inputs)[0]

    # Print the program's output
    print(output)

    # Wait for key press before moving on to the next test
    input("Press Enter to continue...")    