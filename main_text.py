import text_utils as text 

def main():
    '''This function prompt the user for some text and prints the text reversed and then in ALL CAPS.'''
    prompt = input("Please enter some text to play with: ")
    print("Here is the text reversed: " + text.reverse_string(prompt))
    print("Here is the text capitalized: " + text.capitalize_string(prompt))
    
if __name__ == "__main__":
    main()