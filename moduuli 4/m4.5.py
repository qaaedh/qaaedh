# Set the correct username and password
correct_username = "python"
correct_password = "rules"

# Initialize the number of attempts to 0
attempts = 0

# Loop until the user gets the correct username and password or reaches the maximum number of attempts
while attempts < 5:
    # Get the username and password input from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the input is correct
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password. Please try again.")

    # Increment the number of attempts
    attempts += 1

# Check if the user reached the maximum number of attempts
if attempts == 5:
    print("Access denied.")