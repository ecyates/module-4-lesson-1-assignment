import mood_responses

def main():
    '''This function prompts user for their mood and prints a response.'''
    # Prompt user
    mood = input("How are you feeling today? ")
    # Print response
    print(mood_responses.mood_response(mood))

if __name__ == "__main__":
    main()