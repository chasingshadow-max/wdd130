"""
Author: Sunday Edjeba
Course: CSE 111
Assignment: Password Strength Checker

This program checks the strength of user-entered passwords by:
- Checking against a list of common passwords
- Checking password length
- Returning specific strength scores based on requirements
"""

# Lists of allowed character 
LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]


# functions difinition

def word_in_file(word, filename, case_sensitive=False):
    # Check if a word exists in a file.


    # Open the file using UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Read each line in the file
        for line in file:
            file_word = line.strip()  # Remove newline characters

            # Perform case-sensitive or case-insensitive comparison
            if case_sensitive:
                if file_word == word:
                    return True
            else:
                if file_word.lower() == word.lower():
                    return True

    # If no match is found, return False
    return False


def word_has_character(word, character_list):
    #Check if a word contains any character from a given list.


    # Loop through each character in the word
    for char in word:
        if char in character_list:
            return True

    return False


def word_complexity(word):
    """
    Calculate the complexity of a word based on character types.

    Returns:
        int: complexity score from 0 to 4
    """

    complexity = 0

    # Check for each character type and add one point if present
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_strength(password, min_length=10, strong_length=16):
    #Determine the strength of a password.
    # Check if password is a commonly used password
    if word_in_file(password, "toppasswords.txt", False):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Check if password is shorter than 10 characters
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Check if password is longer than 15 characters
    if len(password) > 15:
        print("Password is long, length trumps complexity this is a good password")
        return 5

    # For passwords between 10 and 15 characters, calculate complexity-based score
    score = 1  # Start with 1 for meeting minimum length
    
    # Add complexity score (0-4)
    complexity = word_complexity(password)
    score += complexity
    
    # Ensure score doesn't exceed 5
    if score > 5:
        score = 5
        
    return score


def main():
    # Main user interaction loop.
    # Continues asking for passwords until user enters Q or q.
    
    while True:
        # Prompt user for password
        password = input("\nEnter a password to test (Q to quit): ")

        # Quit condition
        if password.lower() == "q":
            print("Exiting program.")
            break

        # Check password strength
        strength = password_strength(password)

        # Display numeric strength result
        print(f"Strength: {strength}")


# Run the main function when this file is executed directly
if __name__ == "__main__":
    main()