def modify_content(text):
    """
    Function to modify the file content.
    You can customize this! Right now it just converts text to uppercase.
    """
    return text.upper()


def main():
    # Ask user for the input filename
    filename = input("Enter the filename you want to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Create new filename for output
        new_filename = "modified_" + filename

        # Write modified content to new file
        with open(new_filename, "w") as outfile:
            outfile.write(modified)

        print(f"✅ Success! Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
