
# Question 1; File Read & Write Challenge

def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"File '{output_file}' created successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
modify_file("input.txt", "output.txt")


#Question 2;  Error Handling Lab

def read_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            print("\nFile content:\n")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run function
read_file()


