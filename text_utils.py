def reverse_string(s):
    '''This function reverses the characters in a string.'''
    # Take a string, convert it to a list
    s = list(s)
    # Reverse the list
    s.reverse()
    # Convert it back to a string
    s = "".join(s)
    # Return string reversed
    return s

def capitalize_string(s):
    '''This function capitalizes all the letters in a string'''
    return s.upper() # Uses the upper function to capitalize all letters