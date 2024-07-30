def convert_text():
    """
    Prompt the user to choose between converting text to uppercase or lowercase.
    Obtain the input text from the user and perform the requested conversion.
    Print the result.
    """
    options = {
        "1": "uppercase",
        "2": "lowercase"
    }

    while True:
        choice = input("Enter (1) to convert text to uppercase, (2) to convert text to lowercase: ")

        if choice not in options:
            print("Invalid option. Please try again.")
            continue

        conversion = options[choice]
        text = input(f"Enter the text to convert to {conversion}: ")

        if conversion == "uppercase":
            result = text.upper()
        else:
            result = text.lower()

        print(f"The converted text is: {result}")
        break

# Call the function
convert_text()