filename = "output.txt"

with open(filename, "r") as file:
    content = file.read()

print("File contents:")
print(content)
