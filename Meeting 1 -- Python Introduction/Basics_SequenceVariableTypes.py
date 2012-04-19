# Basics_SequenceVariableTypes.py

# list
aList = [1, 15, "Munier"]

# Because list objects are iterable, I can loop through the values like this:
for value in aList:
    print value

# List objects are also mutable, meaning I can change them in place
aList[1] = 35
print aList

# ---------------------------------------------------------------------------
# str
aString = "This is a string!"

# String objects are also iterable, so I can equivalently loop through the
#   characters in a string
for character in aString:
    print character

# But strings are just like in other languages, so you can do all the usual things
print aString.split("a")
print aString.replace("i", "EYE")

# ---------------------------------------------------------------------------

# tuple
aTuple = (1, 15, "Munier")

# Tuples are iterable just like lists, but are immutable so item assignment fails
aTuple[1] = 999 # THIS WILL FAIL! Comment it out to run the code successfully.