######################################################################
# Author: Alex Meadors
# Username: AlexMeadors
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen, the god of modulus
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
birthYear = int(input("What's your birth year?"))
birthYear = birthYear % 12
print(birthYear)
if birthYear == 8:
    print("You're a dragon. Be careful with that morning breath.")
elif birthYear == 9:
    print("You're a snake, the animal, not an insult. This time.")
elif birthYear == 10:
    print("You're a horse, go ride into the sunset.")
elif birthYear == 11:
    print("You're a goat. Not the GOAT unfortunately.")
elif birthYear == 0:
    print("You're a monkey, want a banana?")
elif birthYear == 1:
    print("You're a rooster. Know any good rooster puns?")
elif birthYear == 2:
    print("You're a dog, give a pup a bone.")
elif birthYear == 3:
    print("You're a pig, might want to clean your dorm.")
elif birthYear == 4:
    print("You're a rat. But don't let Vinny hear about it.")
elif birthYear == 5:
    print("You're an ox. I got a funny yoke for you!")
elif birthYear == 6:
    print("You're a tiger, your theme song is going to be messed up with Rocky's. It's too late.")
elif birthYear == 7:
    print("You're a rabbit, gotta say those are some pretty big shoes to fill.")
else:
    print("You did it. You broke everything. I don't know what you did but don't do it again.")
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2
birthYearFriend = int(input("Ok now call your friend over. Hey buddy, what's your birth year?"))

birthYearFriend = birthYearFriend % 12
if birthYearFriend == 8:
    print("You're a dragon. Be careful with that morning breath.")
elif birthYearFriend == 9:
    print("You're a snake, the animal, not an insult. This time.")
elif birthYearFriend == 10:
    print("You're a horse, go ride into the sunset.")
elif birthYearFriend == 11:
    print("You're a goat. Not the GOAT unfortunately.")
elif birthYearFriend == 0:
    print("You're a monkey, want a banana?")
elif birthYearFriend == 1:
    print("You're a rooster. Know any good rooster puns?")
elif birthYearFriend == 2:
    print("You're a dog, give a pup a bone.")
elif birthYearFriend == 3:
    print("You're a pig, might want to clean your dorm.")
elif birthYearFriend == 4:
    print("You're a rat. But don't let Vinny hear about it.")
elif birthYearFriend == 5:
    print("You're an ox. I got a funny yoke for you!")
elif birthYearFriend == 6:
    print("You're a tiger, your theme song is going to be messed up with Rocky's. It's too late.")
elif birthYearFriend == 7:
    print("You're a rabbit, gotta say those are some pretty big shoes to fill.")
else:
    print("You did it. You broke everything. I don't know what you did but don't do it again.")

######################################################################
#CompatScore 5= great 4 = good 3 = possible 2 = whatever 1 = bad  0 = conflict
compatibilityScore = 2
#Start at 2 as its the hardest to make senese of
#Column 1
if birthYear % 2 == 0:
    if birthYear + birthYearFriend == 0 or 4 or 8 or 12 or 16 or 20 or 24:
        compatibilityScore = 5
elif birthYear % 2 == 1:
    if birthYear + birthYearFriend == 2 or 6 or 10 or 14 or 18 or 22 or 26:
        compatibilityScore = 5
#Column 2
if birthYear + birthYearFriend == 9 or 21:
    compatibilityScore = 4
#Column 3
if birthYear - birthYearFriend == 1 or -1 or 11 or -11:
    compatibilityScore = 3
#column 5
if (birthYear - birthYearFriend) or (birthYearFriend - birthYear ) == 6:
    compatibilityScore = 1
#column 6
birthYear = (birthYear + 3) % 12
birthYearFriend = (birthYearFriend + 3) % 12
if birthYear + birthYearFriend == 9 or 21:
    compatibilityScore = 0
if compatibilityScore == 5:
    print("You'll be the best of friends!")
if compatibilityScore == 4:
    print("You'll be great friends.")
if compatibilityScore == 3:
    print("You'll be ok friends")
if compatibilityScore == 2:
    print("You'll be neutral at worst.")
if compatibilityScore == 1:
    print("You're unlikely friends, good for you.")
if compatibilityScore == 0:
    print("How are you guys still friends?!")