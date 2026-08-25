
year = int(input("Enter your birth year: "))
zodiac = (year - 4) % 12

if zodiac == 0:
    sign = "Rat"
elif zodiac == 1:
    sign = "Ox"
elif zodiac == 2:
    sign = "Tiger"
elif zodiac == 3:
    sign = "Rabbit"
elif zodiac == 4:
    sign = "Dragon"
elif zodiac == 5:
    sign = "Snake"
elif zodiac == 6:
    sign = "Horse"
elif zodiac == 7:
    sign = "Goat"
elif zodiac == 8:
    sign = "Monkey"
elif zodiac == 9:
    sign = "Rooster"
elif zodiac == 10:
    sign = "Dog"
else:
    sign = "Pig"

print("Your Chinese Zodiac Sign is:", sign)