from cgitb import text
import os
from turtle import title
os.environ.setdefault('QUIZKER_SETTINGS_MODULE',
                'Quizker_Project.settings')

import django
django.setup()
from Quizker.models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice, QuestionType, QuizAttempt

def populate():
    #ola Peter
    history_quizzes = [
        {"id":"H01","title": "History 101", "creator":"Blathers", "date": "02/02/2017",
        'description':'Test yourself on basic History questions',"question type": "multiple choice", "questions" : history_questions},
        {"id":"H02","title": "Famous Historical Figures", "creator":"Splinter", "date": "03/02/2017",
        'description':'Can you identify the following figures',"question type": "open ended","questions" : history_questions},
        {"id":"H03","title": "History, fact or fiction", "creator":"Speedwagon", "date": "04/12/2019",
        'description':'Can you spot lies from truths',"question type": " True or False", "questions" : history_questions} ]

    science_quizzes = [
        {"id":"S01","title": "Science 101", "creator":"Albert", "date": "09/15/2020",
        'description':'Test yourself on basic Science questions',"question type": "multiple choice","questions" : science_questions},
        {"id":"S02","title": "Marine Biology Masterclass", "creator":"Dr. Jotaro Kujo", "date": "02/09/2017",
        'description':'Brave the depths in this demanding quiz about all things that dwell in the seas',"question type": "multiple choice","questions" : science_questions},
        {"id":"S03","title": "Name the Planet", "creator":"Ziggy Stardust", "date": "12/12/2012",
        'description':'Test your knowledge of the Solar System',"question type": "open ended","questions" : science_questions} ]

    entretainment_quizzes = [
        {"id":"E01","title": "Name The Director", "creator":"Martin", "date": "01/01/2021",
        'description':'Can you name all these famous directors',"question type": "open ended","questions" : entretainment_questions},
        {"id":"E02","title": "Videogame Characters", "creator":"D´Arby", "date": "10/02/2019",
        'description':'Recognize these iconic characters?',"question type": "open ended", "questions" : entretainment_questions},
        {"id":"E03","title": "Guess the Artist", "creator":"Araki", "date": "25/02/2018",
        'description':'Can you match song titles to their respective artists',"question type": "open ended", "questions" : entretainment_questions} ]


    cats = {'History': {'Quizzes': history_quizzes, "id": 1, "description": "All but historical knowledge", "title": "History"},
            'Science': {'Quizzes': science_quizzes, "id": 2,"description": "Test yourself against the sciences","title": "Science"},
            'Entretainment': {'Quizzes': entretainment_quizzes, "id": 3, "description": "Think you know all abut entretainment","title": "Entretainment"} }
    
    history_questions = [
        {"quiz id" : "HO1","id":"HQ01","image": None, "creator":"Blathers", "text": "When did Columbus arrive to the Americas?", "choices" : history_choices},
        {"quiz id" : "HO1","id":"HQ02","image": None, "creator":"Blathers", "text": "What was the name of the first Roman Emperor?", "choices" : history_choices},
        {"quiz id" : "HO1","id":"HQ03","image": None, "creator":"Blathers", "text": "When did WW2 end?", "choices" : history_choices},
        {"quiz id" : "HO2","id":"HQ04","image": None, "creator":"Splinter", "text": "Who is this?"},
        {"quiz id" : "HO2","id":"HQ05","image": None, "creator":"Splinter", "text": "Who is this?"},
        {"quiz id" : "HO2","id":"HQ06","image": None, "creator":"Splinter", "text": "Who is this?"},
        {"quiz id" : "HO3","id":"HQ07","image": None, "creator":"Speedwagon", "text": "Cleopatra was closer to the creation of the smartphone than the building of the great pyramid"},
        {"quiz id" : "HO3","id":"HQ08","image": None, "creator":"Speedwagon","text": "Did the 100-year war last 100 years"},
        {"quiz id" : "HO3","id":"HQ09","image": None, "creator":"Speedwagon", "text": "Potatoes come from Europe"} ]
    
    science_questions = [
        {"quiz id" : "SO1","id":"SQ01","image": None, "creator":"Albert", "text": "What is the atomic number of Hydrogen in the periodic table", "choices" : science_choices},
        {"quiz id" : "SO1","id":"SQ02","image": None, "creator":"Albert", "text": "What is the powerhouse of the cell","choices" : science_choices},
        {"quiz id" : "SO1","id":"SQ03","image": None, "creator":"Albert", "text": "What are the 3 Newton Laws", "choices" : science_choices},
        {"quiz id" : "SO2","id":"SQ04","image": None, "creator":"Dr. Jotaro Kujo", "text": "How many hearts does an octopus have?","choices" : science_choices},
        {"quiz id" : "SO2","id":"SQ05","image": None, "creator":"Dr. Jotaro Kujo", "text": "What species of fish is Nemo?", "choices" : science_choices},
        {"quiz id" : "SO2","id":"SQ06","image": None, "creator":"Dr. Jotaro Kujo", "text": "Which of these marine animlas are mammals?", "choices" : science_choices},
        {"quiz id" : "SO3","id":"SQ07","image": None, "creator":"Ziggy Stardust", "text": "Which planet is this?"},
        {"quiz id" : "SO3","id":"SQ08","image": None, "creator":"Ziggy Stardust", "text": "Which planet is this?"},
        {"quiz id" : "SO3","id":"SQ09","image": None, "creator":"Ziggy Stardust", "text": "Which planet is this?"} ]

    entretainment_questions = [
        {"quiz id" : "EO1","id":"EQ01","image": None, "creator":"Martin", "text": "Who is this director?"},
        {"quiz id" : "EO1","id":"EQ02","image": None, "creator":"Martin", "text": "Who is this director?"},
        {"quiz id" : "EO1","id":"EQ03","image": None, "creator":"Martin","text": "Who is this director?" },
        {"quiz id" : "EO2","id":"EQ04","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "EO2","id":"EQ05","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "EO2","id":"EQ06","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "EO3","id":"EQ07","image": None, "creator":"Araki", "text": "Which artist made this song"},
        {"quiz id" : "EO3","id":"EQ08","image": None, "creator":"Araki", "text": "Which artist made this song"},
        {"quiz id" : "EO3","id":"EQ09","image": None, "creator":"Araki", "text": "Which artist made this song"} ]

    history_choices = [
        {"question id" : "HQO1","id":"HC01","image": None, "correct": False, "text": "999"},
        {"question id" : "HQO1","id":"HC02","image": None, "correct": True, "text": "1492"},
        {"question id" : "HQO1","id":"HC03","image": None, "correct": False,"text": "1250" },
        {"question id" : "HQO1","id":"HC04","image": None, "correct": False, "text": "1450"},
        {"question id" : "HQO2","id":"HC05","image": None, "correct": False, "text": "Cesar"},
        {"question id" : "HQO2","id":"HC06","image": None, "correct": False, "text": "Nero"},
        {"question id" : "HQO2","id":"HC07","image": None, "correct": True, "text": "Octavius"},
        {"question id" : "HQO2","id":"HC08","image": None, "correct": False, "text": "Trajan"},
        {"question id" : "HQO3","id":"HC09","image": None, "correct": True, "text": "1945"},
        {"question id" : "HQO3","id":"HC09","image": None, "correct": False, "text": "1943"},
        {"question id" : "HQO3","id":"HC09","image": None, "correct": False, "text": "1944"},
        {"question id" : "HQO3","id":"HC09","image": None, "correct": False, "text": "1946"} ]

    science_choices = [
        {"question id" : "SQO1","id":"SC01","image": None, "correct": False, "text": "23"},
        {"question id" : "SQO1","id":"SC02","image": None, "correct": False, "text": "68"},
        {"question id" : "SQO1","id":"SC03","image": None, "correct": False,"text": "30" },
        {"question id" : "SQO1","id":"SC04","image": None, "correct": True, "text": "1"},
        {"question id" : "SQO2","id":"SC05","image": None, "correct": True, "text": "Mitochondria"},
        {"question id" : "SQO2","id":"SC06","image": None, "correct": False, "text": "Plasma"},
        {"question id" : "SQO2","id":"SC07","image": None, "correct": False, "text": "Esofagus"},
        {"question id" : "SQO2","id":"SC08","image": None, "correct": False, "text": "Cytoplasm"},
        {"question id" : "SQO3","id":"SC09","image": None, "correct": True, "text": "Action and Reaction"},
        {"question id" : "SQO3","id":"SC10","image": None, "correct": False, "text": "Fluidity"},
        {"question id" : "SQO3","id":"SC11","image": None, "correct": False, "text": "Free Fall"},
        {"question id" : "SQO3","id":"SC12","image": None, "correct": False, "text": "Gravity"},

        {"question id" : "SQO4","id":"SC13","image": None, "correct": False, "text": "5"},
        {"question id" : "SQO4","id":"SC14","image": None, "correct": False, "text": "10"},
        {"question id" : "SQO4","id":"SC15","image": None, "correct": True,"text": "3" },
        {"question id" : "SQO4","id":"SC16","image": None, "correct": False, "text": "51"},
        {"question id" : "SQO5","id":"SC17","image": None, "correct": False, "text": "Shark"},
        {"question id" : "SQO5","id":"SC18","image": None, "correct": True, "text": "Clown Fish"},
        {"question id" : "SQO5","id":"SC19","image": None, "correct": False, "text": "Piranha"},
        {"question id" : "SQO5","id":"SC20","image": None, "correct": False, "text": "Orca"},
        {"question id" : "SQO6","id":"SC21","image": None, "correct": True, "text": "Dolphin"},
        {"question id" : "SQO6","id":"SC22","image": None, "correct": False, "text": "Octopus"},
        {"question id" : "SQO6","id":"SC23","image": None, "correct": False, "text": "Seahorse"},
        {"question id" : "SQO6","id":"SC24","image": None, "correct": False, "text": "Blobfish"},
         ]

    entretainment_choices = [
        {"quiz id" : "EO1","id":"EQ01","image": None, "text":"Martin", "text": "Who is this director?"},
        {"quiz id" : "EO1","id":"EQ02","image": None, "text":"Martin", "text": "Who is this director?"},
        {"quiz id" : "EO1","id":"EQ03","image": None, "creator":"Martin","text": "Who is this director?" },
        {"quiz id" : "EO2","id":"EQ04","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "EO2","id":"EQ05","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "EO2","id":"EQ06","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "EO3","id":"EQ07","image": None, "creator":"Araki", "text": "Which artist made this song"},
        {"quiz id" : "EO3","id":"EQ08","image": None, "creator":"Araki", "text": "Which artist made this song"},
        {"quiz id" : "EO3","id":"EQ09","image": None, "creator":"Araki", "text": "Which artist made this song"} ]


    answers = [
        {"question id" : "HQO4","id":"HA01", "answer": "Simon Bolivar", "text": "23"},
        {"question id" : "HQO5","id":"HA02", "answer": "Barack Obama", "text": "68"},
        {"question id" : "HQO6","id":"HA03", "answer": "Winston Churchill","text": "30" },
        {"question id" : "HQ07","id":"HA04", "answer": True, "text": "1"},
        {"question id" : "HQ08","id":"HA05", "answer": False, "text": "Mitochondria"},
        {"question id" : "HQ09","id":"HA06", "answer": False, "text": "Plasma"},
        {"question id" : "SQO7","id":"SA01", "answer": "Saturn", "text": "Esofagus"},
        {"question id" : "SQO8","id":"SA02", "answer": "Venus", "text": "Cytoplasm"},
        {"question id" : "SQO9","id":"SA03", "answer": "Neptune", "text": "Action and Reaction"},
        {"question id" : "EQO1","id":"EC01", "answer": "Quentin Tarantino", "text": "Fluidity"},
        {"question id" : "EQO2","id":"EC02", "answer": "Stanley Kubrick", "text": "Free Fall"},
        {"question id" : "EQO3","id":"EC03", "answer": "Tommy Wiseau", "text": "Gravity"},
        {"question id" : "EQO4","id":"EC04", "answer": "Tails", "text": "Gravity"} ,
        {"question id" : "EQO5","id":"EC05", "answer": "Sephiroth", "text": "Gravity"},
        {"question id" : "EQO6","id":"EC06", "answer": "Solaire", "text": "Gravity"},
        {"question id" : "EQO7","id":"EC07", "answer": "Yes", "text": "Gravity"} ,
        {"question id" : "EQO8","id":"EC08", "answer": "Red Hot Chili Peppers", "text": "Gravity"} ,
        {"question id" : "EQO9","id":"EC09", "answer": "King Crimson", "text": "Gravity"}   ]
    

    for cat, cat_data in cats.items():
        id = cat_data["id"]
        title = cat
        description = cat_data[ "description"]
        c = add_category(id,cat,description)
        for q in cat_data['quizzes']:
            quiz = add_quiz(c, q['id'], q['title'],q["creator"],q["date"],q["description"],q["question type"])
            quiz_id = q["id"]
            for question in q["questions"]:
                if question["quiz_id"] == quiz_id and q["question type"] == "multiple choice":
                    add_multiple_choice(question["id"],quiz,question["image"],question["text"])
                    for choice in question["choices"]:
                        if choice["question id"] == question["question id"]:
                            add_choice(choice["id"], question,choice["text"], choice["correct"])


                elif question["quiz_id"] == quiz_id and q["question type"] == "open ended":
                    for answer in answers:
                        if question["id"] == answer["question id"]:
                            the_answer = answers["answer"]

                    add_open_ended(question["id"],quiz,question["image"],question["text"], the_answer)

                elif question["quiz_id"] == quiz_id and q["question type"] == "True or False":
                    for answer in answers:
                        if question["id"] == answer["question id"]:
                            the_answer = answers["answer"]

                    add_true_false(question["id"],quiz,question["image"],question["text"], the_answer)

def add_question(id,quiz, image, text):
    #Chech get_or_create inputs to properly calll function
    qe = Question.objects.get_or_create(parameter=quiz, title=title)[0]
    #Do questions have url?
    qe.save()
    return qe

def add_multiple_choice(id,quiz, image, text):
    qe = Question.objects.get_or_create(id = id, quiz=quiz, image=image,text = text)[0]
    qe.save()
    return qe

def add_choice(id,question, text, correct):
    qe = Choice.objects.get_or_create(id = id, question=question,text = text, correct = correct)[0]
    qe.save()
    return qe


def add_true_false(id,quiz, image, text, answer):
    qe = Question.objects.get_or_create(id = id, quiz=quiz, image=image,text = text, answer = answer)[0]
    qe.save()
    return qe

def add_open_ended(id,quiz, image, text, answer):
    qe = Question.objects.get_or_create(id = id, quiz=quiz, image=image,text = text, answer = answer)[0]
    qe.save()
    return qe

def add_quiz(cat,id,title,creator,date,description,QuestionType):
    qi = Quiz.objects.get_or_create(category = cat, id=id,title=title, creator = creator,
    date = date,description=description,QuestionType=QuestionType)[0]
    qi.save()
    return qi

def add_category(id,title,description):
    c = Quiz.objects.get_or_create(id=id,title=title,descriptipn = description)[0]
    c.save()
    return c

















if __name__ == '__main__':
    print('Starting Quizker population script...')
    populate()