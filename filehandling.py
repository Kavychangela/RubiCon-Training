filename = "student.txt"

try:
    # 1. Create the file
    with open(filename, "x") as file:
        file.write("Name: Yogesh\n")
        file.write("Course: Python\n")
        file.write("Age: 25\n")

    print("1. File created successfully")

except FileExistsError:
    print("1. File already exists")


# 2. Write data to the file
with open(filename, "w") as file:
    file.write("Name: Yogesh\n")
    file.write("Course: Python\n")
    file.write("Age: 25\n")

print("2. File written successfully")


# 3. Read the complete file
with open(filename, "r") as file:
    data = file.read()

print("3. File read successfully")
print(data)


# 4. Read all lines
with open(filename, "r") as file:
    lines = file.readlines()

print("4. All Lines:")
print(lines)