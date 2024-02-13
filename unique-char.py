
# - - - - - - This function takes a string as a parameter and determines if each character in the string is unique.     - - - - - - #
# - - - - - - If each character only appears once in the string, the function returns True. Otherwise, it returns False.- - - - - - #

def isUnique(string):
    from collections import defaultdict
    char_dict = defaultdict(int)    # Creating a dictionary to store characters
    unique = True                   # Initializing unique value as True
    for char in string:
        if char in char_dict:       # If char already exists in the dictionary, it changes unique value to False.
            unique = False
        else:
            char_dict[char]         # If char doesn't exist, it creates it in the dictionary.
    return unique
