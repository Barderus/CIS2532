''' 5.13 - Word or Phrase to Phone-Number generator
Write a script that produces the possible phone number for the given seven-letter string.
    Ex: 738-2273 = PETCARE
        244-3282 = BIGDATA
        686-2377 = NUMBERS
    Digit       Letters
      2          A B C         
      3          D E F
      4          G H I 
      5          J K L
      6          M N O
      7          P R S
      8          T U V
      9          W X Y
'''
def generate_phone_numbers(letters):
    digit_to_letters = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y']
    }
    first_three_letters = letters[:3]
    last_four_letters = letters[3:]
    # Step 1: Convert the first three letters into digits
    first_three_digits = ''
    for letter in first_three_letters:
        for digit, chars in digit_to_letters.items():
            if letter.upper() in chars:
                first_three_digits += digit
                break

    # Step 2: Convert the last four letters into digits
    last_four_digits = ''
    for letter in last_four_letters:
        for digit, chars in digit_to_letters.items():
            if letter.upper() in chars:
                last_four_digits += digit
                break

    # Step 3: Combine the first three digits and last four digits with a hyphen
    return f"{first_three_digits}-{last_four_digits}"

def main():
    while True:
        word = input("Enter a word (6 letters): ")
        if len(word) == 7 and word.isalpha():  # Check if input is exactly 6 letters and contains only alphabetic characters
            break
        else:
            print("Please enter exactly 6 alphabetic letters.")

    possible_numbers = generate_phone_numbers(word)
    print(f"Possible phone number for '{word}': {possible_numbers}")


if __name__ == "__main__":
    main()


