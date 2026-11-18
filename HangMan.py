import getpass
import numpy as np 
lives = 6 
print('typing is hidden')
secret_w = getpass.getpass('Enter secret word ').lower()
total_char = len(secret_w)
secret_w_n = 0
while  secret_w_n < total_char and lives > 0 :
    a = input('Enter letter ').lower()
    if a in secret_w:
        secret_w_n += 1
        print('Correct')
    else:
        lives = lives - 1
        print(f"Wrong! You have {lives} lives left.")
    print("❤️ " * lives)
if secret_w_n >= total_char:
    print('Guesser wins')   
    print(secret_w)

if lives == 0:
    print('The answer was:',secret_w)