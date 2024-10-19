user_input = input("Enter a string: ")

cleaned_input = user_input.lower()

reversed_input = cleaned_input[::-1]

if cleaned_input == reversed_input:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')

