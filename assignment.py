# 1. A simple python program to
# check whether a year is a leap or not
year = 2025
if year % 400 == 0:
    print("leap year")
else :
    print("not leap year")

# A python program that checks whether a letter is a vowel or a consonant
letter = "d                                                                                                                                                                                 "
if letter in ("a", "e", "i", "o", "u"):
    print("vowel")
elif letter in ("A", "E", "I", "O", "U"):
    print("vowel")
else:
    print("consonant")
#method 2
letter = 'z'
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("vowel")
else :
    print("consonant")