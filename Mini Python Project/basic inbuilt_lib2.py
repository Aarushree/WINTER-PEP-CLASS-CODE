# 1.generate random password
# 2. check password strength
# 3.count character used in password
# 4.gives a strengh score using math
# 5. saves the result in a file using os
import random      #----------------------> importing random
import math        #----------------------> importing math
import os          #----------------------> importing os
import re
from collections import Counter

#---------------------- Generate random password ----------------------
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$"
pass_length = 8
password = "".join(random.choice(chars) for _ in range(pass_length))

print("Password:", password)

#---------------------- Check password strength ----------------------
upper = len(re.findall(r"[A-Z]", password))
lower = len(re.findall(r"[a-z]", password))
digit = len(re.findall(r"[0-9]", password))
special = len(re.findall(r"[@#$]", password))

#---------------------- Count characters ----------------------
char_count = Counter(password)

#---------------------- Strength score using math ----------------------
score = upper + lower + digit + (special * 2)
strength_score = math.ceil(score / pass_length)

if strength_score <= 2:
    strength = "Weak"# Password is weak if score is very low
elif strength_score <= 4:
    strength = "Medium"# Password is medium if score is average
else:
    strength = "Strong"# Password is Strong if score is high

#---------------------- Save result using os ----------------------
if not os.path.exists("password_reports"):
    os.mkdir("password_reports")

file_path = os.path.join("password_reports", "password_report.txt")

file = open(file_path, "w") # Opens the file in write mode
file.write(f"Password: {password}\n")# Writes password to the file
file.write(f"Uppercase Letters: {upper}\n")#upercase count
file.write(f"Lowercase Letters: {lower}\n")#lowercase count
file.write(f"Digits: {digit}\n")#number count
file.write(f"Special Characters: {special}\n")#special count
file.write(f"Strength Score: {strength_score}\n")#strenght score
file.write(f"Password Strength: {strength}\n")#final strenght result
file.write("Character Count:\n")

for ch, count in char_count.items():
    file.write(f"{ch} : {count}\n") #it will  write each character and its count

file.close()

#---------------------- Output ----------------------
print(strength)
print(strength_score)
print(char_count)
print(file_path)
