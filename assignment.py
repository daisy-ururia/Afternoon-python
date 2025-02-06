# 1. A simple python program to
# check whether a year is a leap or not

# A python program that checks whether a letter is a vowel or a consonant
year = 2025
if year % 400 == 0:
    print("leap year")
else :
    print("not leap year")

vowel = "aeiouAEIOU"
letter = input("enter a letter ; ")

if letter in vowel:
    print("vowel")

else :
    print("consonant")
