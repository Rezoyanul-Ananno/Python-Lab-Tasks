try:
    file_name = "example.txt"

    # Write
    with open(file_name, "w") as file:
        file.write("Hello, this is the first line.\n")

    # Append
    with open(file_name, "a") as file:
        file.write("This line is added using append.\n")

    # Read
    with open(file_name, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)

    # Create
    with open("new_file.txt", "x") as file:
        file.write("This is a newly created file.")

    print("Files created successfully.")

except FileExistsError:
    print("Error: File already exists.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected error:", e)