import random
import string
length = int(input("Enter the length of the password you want to generate: "))
password=[]
characters = string.ascii_letters + string.digits + string.punctuation
for i in range(length):
    randomchar = random.choice(characters)
    password.append(randomchar)
print("Generated Password: ", ''.join(password))