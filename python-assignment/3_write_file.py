filename = "output.txt"

with open(filename, "w") as file:
    file.write("Hello, this is a Python file writing example.\n")
    file.write("This is the second line.\n")
    file.write("Python makes file handling easy!\n")

print(f"Content written to '{filename}' successfully.")
