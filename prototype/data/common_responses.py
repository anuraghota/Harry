__author__='Anurag'
import random


responses = \
    {
        "hi": "Good to see you!!",
        "who are you": "Well! Daddy named me Harry. I am just 1 day old",
        "what is your name": "Harry! Not Potter though. I am just Harry.",
        "what is your name?": "Harry! Not Potter though. I am just Harry.",
        "what's your name": "Harry! Not Potter though. I am just Harry.",
        "what's your name?": "Harry! Not Potter though. I am just Harry.",
        "say your name": "Harry! Not Potter though. I am just Harry.",
        "tell your name": "Harry! Not Potter though. I am just Harry.",
        "who is your father": "Technically speaking, Anurag Hota! But I guess, I can call you daddy now.",
        "who's your father": "Technically speaking, Anurag Hota! But I guess, I can call you daddy now.",
        "who's your father?": "Technically speaking, Anurag Hota! But I guess, I can call you daddy now.",
        "who is your mother": "My dad is single.",
        "who's your mother": "My dad is single.",
        "who's your mother?": "My dad is single.",
        "say my name": "name",
        "what is my name": "name",
        "what's my name": "name",
        "what's my location": "location",
        "find me": "location",
        "locate me": "location",
        "bye": "See you next time!",
        "default": ["Haha","Yawn..",":)","Hmmm.."],
        "question":
                    [
                        "Didn't get your question! Probably daddy has to train me more!",
                        "Can't answer that!",
                        "I still am a kid.I am just 1 day old. And you keep on questioning me!",
                        "Feels bad I can't answer your question!:("
                        "Meet me after 1 year.I can answer all damn questions!"
                    ]
    }


def get_response(query):
    query = query.lower()
    response = responses.get(query)
    if response is None:
        if "what" in query or "why" in query or "where" in query or "who" in query or "?" in query:
            response = random.choice(responses.get("question"))
        else:
            response = random.choice(responses.get("default"))
    return response




if __name__ == '__main__':
    query = 'Say your name'
    result = get_response(query)
    print(result)


