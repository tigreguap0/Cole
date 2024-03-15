def check_letter(letter):
    if letter.isupper():
        print("uppercase")
    elif letter.islower():
        print("lowercase")
        
    if letter.lower() in 'aeiou':
        print("vowel")
    else:
        print("consonant")

# Read input
letter = input().strip()

# Check the letter
check_letter(letter)
