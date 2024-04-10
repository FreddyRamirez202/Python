string1 = "Hi I'm Freddy"
string2 = "Hi again"

#Convert to uppercase
uppercase = string1.upper()

#Convert to lowercase
lowercase = string1.lower()

#Firts letter in uppercase
first_letter_uppercase = string1.capitalize()

#We look for a string in another string,If there are no matches, returns - 1
find = string1.find("H")

#We look for a string in another string, if there are no matches, throw an exception
index = string1.index("d")

#If numeric, return true, otherwise return false
numeric = string1.isnumeric()

#If it is alpha numeric we return true, if not we return false
alphanumeric = string1.isalpha()

#We count the number of matches of a string within another string returns the number of matches
mathcounting = string1.count("d")

#We count how many characters are in a string
characterscounting = len(string1)

#We check if a string starts with another given string if so, it returns true
startwith = string1.startswith("h")

#We check if a string ends with another given string if so, return true
endwith = string1.endswith("ddy")

#Replaces a piece of the given string by another given string
newstring = string1.replace("Freddy", "Alexis")

#separate strings with the string we pass it
separatestring = string1.split(",")
print(separatestring[0])