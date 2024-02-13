
# - - - - - - This function checks if a number is a palindrome. Takes an int as a parameter and checks if its the same number forwards and backwards. - - - - - - #
def isPalindrome(x):
    palindrome = True                           # Initializing palindrome to True
    string = str(x)                             # Casting int to str in order to check each character
    for i in range(0, len(string)):
        if string[i] == string[-(i +1)]:        # Checking if the character at i and the character at -i are equal.
            palindrome = True                   # If each character is the same, the palindrome stays as true.
        else:
            return False                        # Returns false immediately if characters differ.
    return palindrome
