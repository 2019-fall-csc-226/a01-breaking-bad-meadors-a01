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
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
birthYear = int(input("What's your birth year?"))

if birthYear == 2000:
    print("You're a dragon. Be careful with that morning breath.")
elif birthYear == 2001:
    print("You're a snake, the animal, not an insult. This time.")
elif birthYear == 2002:
    print("You're a horse, go ride into the sunset.")
elif birthYear == 2003:
    print("You're a goat. Not the GOAT unfortunately.")
elif birthYear == 2004:
    print("You're a monkey, want a banana?")
elif birthYear == 2005:
    print("You're a rooster. Know any good rooster puns?")
elif birthYear == 2006:
    print("You're a dog, give a pup a bone.")
elif birthYear == 2007:
    print("You're a pig, might want to clean your dorm.")
elif birthYear == 2008:
    print("You're a rat. But don't let Vinny hear about it.")
elif birthYear == 2009:
    print("You're an ox. I got a funny yoke for you!")
elif birthYear == 2010:
    print("You're a tiger, your theme song is going to be messed up with Rocky's. It's too late.")
elif birthYear == 2011:
    print("You're a rabbit, gotta say those are some pretty big shoes to fill.")
else:
    print("You're either 8 or younger or 20 and older. Just go Google it.")
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
