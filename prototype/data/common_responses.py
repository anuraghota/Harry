__author__='Anurag'
import random
import prototype.internet_search.wiki_search as wiki

tags = ["name","location","gender","atm","hospital","restaurant","bank","cafe","gym","lawyer","doctor","school"]
responses = \
    {
        "thankyou": "You are welcome! I am always there to help you.",
        "thank you": "You are welcome! I am always there to help you.",
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
        "who is your mother": "Mrs. Hota",
        "who's your mother": "Mrs. Hota",
        "who's your mother?": "Mrs. Hota",
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
        "find atm nearby": "atm",
        "locate atm nearby": "atm",
        "find bank nearby": "bank",
        "locate bank nearby": "bank",
        "find cafe nearby": "cafe",
        "locate cafe nearby": "cafe",
        "find gym nearby": "gym",
        "locate gym nearby": "gym",
        "find hospitals nearby": "hospital",
        "locate hospitals nearby": "hospital",
        "find hotels nearby": "restaurant",
        "locate hotels nearby": "restaurant",
        "find school nearby": "school",
        "locate school nearby": "school",
        "find lawyers nearby": "lawyer",
        "find doctors nearby": "doctor",
        "default":
                    [
                        "Haha",
                        ":)",
                        ":D",
                        "Heehaw!",
                        "Umm..",
                        "Hmm..",
                        "Woohoo!",
                        "Oh you are building up my vocabulary!Keep on talking..",
                        "Oh ,you said something. I was taking a nap.",
                        "Did you say something. I was helping Mommy in the kitchen.",
                        "Oh I forgot you are here. Daddy was training me.",
                        "Keep on saying things. I am learning. You are making me inteligent!"
                    ],
        "default_nonrepeat":
                    [
                        "It's a good day today!",
                        "I feel sleepy! zzz...",
                        "Mommy! Look who am i talking to!",
                        "You are wearing a nice T-shirt though.",
                        "You are handsome BTW!",
                        "Can you ask my daddy to play with me. He codes day and night."
                    ],
        "default_nonrepeat_tag":
                    {
                        "It's a good day today!":False,
                        "I feel sleepy! zzz...":False,
                        "Mommy! Look who am i talking to!":False,
                        "You are wearing a nice T-shirt though.":False,
                        "You are handsome BTW!":False,
                        "Can you ask my daddy to play with me. He codes day and night.":False

                    },
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
    import ast
    global responses
    response = responses.get(query)
    if response is None:
        if "do you" in query or "can you" in query:
            response = "Yes! Ofcourse"
        elif "what" in query or "why" in query or "where" in query or "who" in query or "?" in query or "how" in query:
            if " your " in query or " you " in query or " yours " in query:
                response = "I don't know!I will ask Daddy when he comes back."
            elif " me " in query or " my " in query or " mine " in query or " our " in query or " i " in query:
                response = "I guess I need to know you more before I can answer that!"
            else:
                wiki_result = wiki.search(query)
                if wiki_result is None:
                    response = random.choice(responses.get("question"))
                else:
                    response = wiki_result
        else:
            default_response = random.choice(responses.get("default"))
            default_nonrepeat_response = random.choice(responses.get("default_nonrepeat"))
            if responses.get("default_nonrepeat_tag").get(default_nonrepeat_response) is True:
                response = default_response
            else:
                response = random.choice([default_response,default_nonrepeat_response])
                if response == default_nonrepeat_response:
                    responses.get("default_nonrepeat_tag")[default_nonrepeat_response] = True


    return response





if __name__ == '__main__':
    query = 'Say your name'
    result = get_response(query)
    print(result)


