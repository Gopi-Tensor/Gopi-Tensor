# Convert vowels in a string to uppercase

# Iterate through each character in the string

# Check if the character is a vowel (a, e, i, o, u)

# If it is a vowel, convert it to uppercase
def convert_vowel_to_upper(string: str):
    vowels = 'aeiou'  # Can be a string directly
    new_string = []  # Use a list for building the new string for better performance

    for char in string.lower():  # Convert to lower once and iterate
        if char in vowels:
            new_string.append(char.upper())  # Append the uppercase version if it's a vowel
        else:
            new_string.append(char)  # Otherwise, append the char as it is

    return ''.join(new_string)  # Join all characters in the list to form the final string

result = convert_vowel_to_upper(string='gOpi')
print(result)

