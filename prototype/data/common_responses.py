__author__='Anurag'
import random
import prototype.internet_search.wiki_search as wiki


responses = \
    {
        "hi": "Good to see you!!",
        "who are you": "Well! Daddy named me Harry. I am just 1 day old",
        "and yours": "Harry! Not Potter though. I am just Harry.",
        "what is your name": "Harry! Not Potter though. I am just Harry.",
        "what is your name?": "Harry! Not Potter though. I am just Harry.",
        "what's your name": "Harry! Not Potter though. I am just Harry.",
        "what's your name?": "Harry! Not Potter though. I am just Harry.",
        "say your name": "Harry! Not Potter though. I am just Harry.",
        "tell your name": "Harry! Not Potter though. I am just Harry.",
        "who is your father": "Technically speaking, Anurag Hota! But I guess, I can call you daddy now.",
        "who's your father": "Technically speaking, Anurag Hota! But I guess, I can call you daddy now.",
        "who's your father?": "Technically speaking, Anurag Hota! But I guess, I can call you daddy now.",
        "who's your daddy": "Technically speaking, Anurag Hota! But I guess, I can call you daddy now.",
        "who is your mother": "My dad is single.",
        "who's your mother": "My dad is single.",
        "who's your mother?": "My dad is single.",
        "say my name": "name",
        "what is my name": "name",
        "what's my name": "name",
        "what's my location": "location",
        "what's my gender": "gender",
        "what is my gender": "gender",
        "am i male or female": "gender",
        "find me": "location",
        "locate me": "location",
        "bye": "See you next time!",
        "default":
                    [
                        "Haha",
                        ":)",
                        ":D",
                        ":')",
                        "It's a good day today!",
                        "I feel sleepy! zzz...",
                        "Mommy! Look who am i talking to!"
                        "You are wearing a nice T-shirt though.",
                        "You are handsome BTW!",
                        "Can you ask my daddy to play with me. He codes day and night."
                    ],
        "question":
                    [
                        "Didn't get your question! Probably daddy has to train me more!",
                        "Can't answer that!",
                        "I still am a kid.I am just 1 day old. And you keep on questioning me!",
                        "Feels bad I can't answer your question!:(",
                        "Meet me after 1 year.I can answer all damn questions!"
                    ]
    }


def get_response(query):
    query = query.lower()
    response = responses.get(query)
    if response is None:
        if "do you" in query or "can you" in query:
            response = "No!!!"
        elif "what" in query or "why" in query or "where" in query or "who" in query or "?" in query:
            wiki_result = wiki.search(query)
            if wiki_result is None:
                response = random.choice(responses.get("question"))
            else:
                response = wiki_result
        else:
            response = random.choice(responses.get("default"))
    return response





if __name__ == '__main__':
    query = 'Say your name'
    result = get_response(query)
    print(result)


