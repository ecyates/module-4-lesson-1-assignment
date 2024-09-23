def mood_response(mood):
    '''This function takes a mood and if it's in the moods list, returns an appropriate response. 
    Otherwise, it alerts the user that it's not sure how to respond.'''
    # Define moods and responses.
    moods = {
        'happy': "That's fantastic! I'm so happy for you. Tell me more about what's making you feel this way!",
        'sad': "I'm really sorry to hear that. Do you want to talk about what's on your mind? I'm here for you.",
        'frustrated': "That sounds really frustrating. Is there anything I can do to help or make things easier for you?",
        "anxious" : "I understand that you're feeling anxious. Take a deep breath. I'm sure you've got this. Do you want to go over things together?",
        'angry' : "It sounds like you're really upset. I'm here if you need to vent or talk it through.",
        'confused' : "It's okay to feel unsure sometimes. Do you want to work through this together and see if we can find some clarity?",
        'lonely' : "I'm really sorry you're feeling this way. Do you want to meet up or talk for a bit? I'm always here if you need someone to talk to.",
        'tired' : "You've been doing a lot. Make sure to take some time for yourself. How about taking a short break or a nap?",
        'grateful' : "That means a lot—thank you! I'm so glad I could help. Let me know if there's anything else you need.",
        'motivated' : "That's amazing! I love your energy. How can I support you in achieving your goals?",
        'embarrassed' : "I know it feels tough right now, but everyone makes mistakes. It's how we learn and grow. I'm here for you, no judgment.",
        'bored' : "Maybe we can switch things up a bit? Let's find something new or fun to do that might re-energize you.",
        'proud' : "That's such a great achievement! You've worked hard, and it shows—well done!",
        'guilty' : "It's natural to feel guilty sometimes, but try not to be too hard on yourself. What's done is done. Is there anything you'd like to do differently next time?",
        'hopeful' : "I love how positive you're feeling! It's so refreshing to hear. What are you looking forward to most?"
        }
    # If the mood is in the list, return response
    if mood.lower() in moods.keys():
        return moods[mood.lower()]
    # Otherwise, replies that it's not sure how to respond.
    else:
        return "I'm not sure how to respond to that."