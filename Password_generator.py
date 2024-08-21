#Random Password Generator 
import random
import string

# Define the character set including digits, letters, and punctuation
password = string.digits + string.ascii_letters + string.punctuation

# Initialize an empty string to hold the generated password
p = ""

# Generate a password of length 8 by randomly selecting characters from the set
for i in range(8):
    p += random.choice(password)

# Print the generated password
print("Your password is:", p)
