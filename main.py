import subprocess

# Ask the user for the filename
filename = input("Enter the filename (without extension): ")

# Add the file extension
input_file = filename + ".txt"
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
        inputs = file.read()

# Invoke the second Python program with the inputs
process = subprocess.Popen(['python', prog], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
process.stdin.write(inputs.encode())
process.stdin.flush()

# Read the output from the program
output = process.stdout.read().decode()

# Close the input stream and wait for the program to finish
process.stdin.close()
process.wait()

# Print the program's output
print(output)
