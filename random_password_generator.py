#lets create a simple password generator 

import random 
import string

#define a function to generate the password

def generate_pw(length=12, use_uppercase=True, use_digits=True, use_punctuation=True):
    #defining the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation 

    # Create the pool of characters to choose from
    char_pool = lowercase
    if use_uppercase:
        char_pool += uppercase
    if use_digits:
        char_pool += digits
    if use_punctuation:
        char_pool += punctuation
    # Generate the random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

if __name__ == '__main__':
    # Generate a random password with default settings (12 characters, includes uppercase, digits, punctuation)
    password = generate_pw()
    print(f"Generated Password: {password}")

# i will do half tomorrow 

