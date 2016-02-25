__author__='Anurag'

question_tags = {}
questions = \
    {
        "name": "What is your name?",
        "age": "What's your age?",
        "gender": "Are you male or female?",
        "marriage_status": "Are you single?",
        "work_status": "Where do you work?",
        "home_adrress": "Your home address?",
        "office_adrress": "Your office address?"
    }

def set_tag(tag):
    global question_tags
    question_tags[tag] = True


