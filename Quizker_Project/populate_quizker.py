from cgitb import text
import os
from turtle import title
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                'Quizker_Project.settings')

import django
django.setup()
from Quizker.models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice, QuizAttempt
from django.contrib.auth.models import User

def populate():
    #ola Peter

    history_choices = [
        {"question id" : "1","id":"1","image": None, "correct": False, "text": "999"},
        {"question id" : "1","id":"2","image": None, "correct": True, "text": "1492"},
        {"question id" : "1","id":"3","image": None, "correct": False,"text": "1250" },
        {"question id" : "1","id":"4","image": None, "correct": False, "text": "1450"},
        {"question id" : "2","id":"5","image": None, "correct": False, "text": "Cesar"},
        {"question id" : "2","id":"6","image": None, "correct": False, "text": "Nero"},
        {"question id" : "2","id":"7","image": None, "correct": True, "text": "Octavius"},
        {"question id" : "2","id":"8","image": None, "correct": False, "text": "Trajan"},
        {"question id" : "3","id":"9","image": None, "correct": True, "text": "1945"},
        {"question id" : "3","id":"10","image": None, "correct": False, "text": "1943"},
        {"question id" : "3","id":"11","image": None, "correct": False, "text": "1944"},
        {"question id" : "3","id":"12","image": None, "correct": False, "text": "1946"} ]

    science_choices = [
        {"question id" : "10","id":"13","image": None, "correct": False, "text": "23"},
        {"question id" : "10","id":"14","image": None, "correct": False, "text": "68"},
        {"question id" : "10","id":"15","image": None, "correct": False,"text": "30" },
        {"question id" : "10","id":"16","image": None, "correct": True, "text": "1"},
        {"question id" : "11","id":"17","image": None, "correct": True, "text": "Mitochondria"},
        {"question id" : "11","id":"18","image": None, "correct": False, "text": "Plasma"},
        {"question id" : "11","id":"19","image": None, "correct": False, "text": "Esofagus"},
        {"question id" : "11","id":"20","image": None, "correct": False, "text": "Cytoplasm"},
        {"question id" : "12","id":"21","image": None, "correct": True, "text": "Action and Reaction"},
        {"question id" : "12","id":"22","image": None, "correct": False, "text": "Fluidity"},
        {"question id" : "12","id":"23","image": None, "correct": False, "text": "Free Fall"},
        {"question id" : "12","id":"24","image": None, "correct": False, "text": "Gravity"},

        {"question id" : "13","id":"25","image": None, "correct": False, "text": "5"},
        {"question id" : "13","id":"26","image": None, "correct": False, "text": "10"},
        {"question id" : "13","id":"27","image": None, "correct": True,"text": "3" },
        {"question id" : "13","id":"28","image": None, "correct": False, "text": "51"},
        {"question id" : "14","id":"29","image": None, "correct": False, "text": "Shark"},
        {"question id" : "14","id":"30","image": None, "correct": True, "text": "Clown Fish"},
        {"question id" : "14","id":"31","image": None, "correct": False, "text": "Piranha"},
        {"question id" : "14","id":"32","image": None, "correct": False, "text": "Orca"},
        {"question id" : "15","id":"33","image": None, "correct": True, "text": "Dolphin"},
        {"question id" : "15","id":"34","image": None, "correct": False, "text": "Octopus"},
        {"question id" : "15","id":"35","image": None, "correct": False, "text": "Seahorse"},
        {"question id" : "15","id":"36","image": None, "correct": False, "text": "Blobfish"},
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
        {"question id" : "4","id":"1", "answer": "Simon Bolivar", "text": "23"},
        {"question id" : "5","id":"2", "answer": "Barack Obama", "text": "68"},
        {"question id" : "6","id":"3", "answer": "Winston Churchill","text": "30" },
        {"question id" : "7","id":"4", "answer": True, "text": "1"},
        {"question id" : "8","id":"5", "answer": False, "text": "Mitochondria"},
        {"question id" : "9","id":"6", "answer": False, "text": "Plasma"},
        {"question id" : "16","id":"7", "answer": "Saturn", "text": "Esofagus"},
        {"question id" : "17","id":"8", "answer": "Venus", "text": "Cytoplasm"},
        {"question id" : "18","id":"9", "answer": "Neptune", "text": "Action and Reaction"},
        {"question id" : "19","id":"10", "answer": "Quentin Tarantino", "text": "Fluidity"},
        {"question id" : "20","id":"11", "answer": "Stanley Kubrick", "text": "Free Fall"},
        {"question id" : "21","id":"12", "answer": "Tommy Wiseau", "text": "Gravity"},
        {"question id" : "22","id":"13", "answer": "Tails", "text": "Gravity"} ,
        {"question id" : "23","id":"14", "answer": "Sephiroth", "text": "Gravity"},
        {"question id" : "24","id":"15", "answer": "Solaire", "text": "Gravity"},
        {"question id" : "25","id":"16", "answer": "Yes", "text": "Gravity"} ,
        {"question id" : "26","id":"17", "answer": "Red Hot Chili Peppers", "text": "Gravity"} ,
        {"question id" : "27","id":"18", "answer": "King Crimson", "text": "Gravity"} ]

    history_questions = [
        {"quiz id" : "1","id":"1","image": None,  "text": "When did Columbus arrive to the Americas?", "choices" : history_choices},
        {"quiz id" : "1","id":"2","image": None,  "text": "What was the name of the first Roman Emperor?", "choices" : history_choices},
        {"quiz id" : "1","id":"3","image": None, "text": "When did WW2 end?", "choices" : history_choices},
        {"quiz id" : "2","id":"4","image": None,  "text": "Who is this?"},
        {"quiz id" : "2","id":"5","image": None,  "text": "Who is this?"},
        {"quiz id" : "2","id":"6","image": None,  "text": "Who is this?"},
        {"quiz id" : "3","id":"7","image": None, "text": "Cleopatra was closer to the creation of the smartphone than the building of the great pyramid"},
        {"quiz id" : "3","id":"8","image": None, "text": "Did the 100-year war last 100 years"},
        {"quiz id" : "3","id":"9","image": None, "text": "Potatoes come from Europe"} ]
    
    science_questions = [
        {"quiz id" : "4","id":"10","image": None, "creator":"Albert", "text": "What is the atomic number of Hydrogen in the periodic table", "choices" : science_choices},
        {"quiz id" : "4","id":"11","image": None, "creator":"Albert", "text": "What is the powerhouse of the cell","choices" : science_choices},
        {"quiz id" : "4","id":"12","image": None, "creator":"Albert", "text": "What are the 3 Newton Laws", "choices" : science_choices},
        {"quiz id" : "5","id":"13","image": None, "creator":"Dr. Jotaro Kujo", "text": "How many hearts does an octopus have?","choices" : science_choices},
        {"quiz id" : "5","id":"14","image": None, "creator":"Dr. Jotaro Kujo", "text": "What species of fish is Nemo?", "choices" : science_choices},
        {"quiz id" : "5","id":"15","image": None, "creator":"Dr. Jotaro Kujo", "text": "Which of these marine animlas are mammals?", "choices" : science_choices},
        {"quiz id" : "6","id":"16","image": None, "creator":"Ziggy Stardust", "text": "Which planet is this?"},
        {"quiz id" : "6","id":"17","image": None, "creator":"Ziggy Stardust", "text": "Which planet is this?"},
        {"quiz id" : "6","id":"18","image": None, "creator":"Ziggy Stardust", "text": "Which planet is this?"} ]

    entretainment_questions = [
        {"quiz id" : "7","id":"19","image": None, "creator":"Martin", "text": "Who is this director?"},
        {"quiz id" : "7","id":"20","image": None, "creator":"Martin", "text": "Who is this director?"},
        {"quiz id" : "7","id":"21","image": None, "creator":"Martin","text": "Who is this director?" },
        {"quiz id" : "8","id":"22","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "8","id":"23","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "8","id":"24","image": None, "creator":"D´Arby", "text": "Who is this character?"},
        {"quiz id" : "9","id":"25","image": None, "creator":"Araki", "text": "Which artist made this song"},
        {"quiz id" : "9","id":"26","image": None, "creator":"Araki", "text": "Which artist made this song"},
        {"quiz id" : "9","id":"27","image": None, "creator":"Araki", "text": "Which artist made this song"} ]

    
    history_quizzes = [
        {"id":"1","title": "History 101", "likes":15, "date": "2017-02-02",
        'description':'Test yourself on basic History questions',"question type": "MultipleChoice", "questions" : history_questions},
        {"id":"2","title": "Famous Historical Figures", "likes":60, "date": "2017-03-02",
        'description':'Can you identify the following figures',"question type": "OpenEnded","questions" : history_questions},
        {"id":"3","title": "History, fact or fiction", "likes": 80, "date": "2019-04-05",
        'description':'Can you spot lies from truths',"question type": " TrueOrFalse", "questions" : history_questions} ]

    science_quizzes = [
        {"id":"4","title": "Science 101", "likes": 10, "date": "2020-09-15",
        'description':'Test yourself on basic Science questions',"question type": "MultipleChoice","questions" : science_questions},
        {"id":"5","title": "Marine Biology Masterclass", "likes": 89, "date": "2017-02-09",
        'description':'Brave the depths in this demanding quiz about all things that dwell in the seas',"question type": "MultipleChoice","questions" : science_questions},
        {"id":"6","title": "Name the Planet", "likes":50, "date": "2012-12-12",
        'description':'Test your knowledge of the Solar System',"question type": "OpenEnded","questions" : science_questions} ]

    entretainment_quizzes = [
        {"id":"7","title": "Name The Director", "likes":24, "date": "2021-01-01",
        'description':'Can you name all these famous directors',"question type": "OpenEnded","questions" : entretainment_questions},
        {"id":"8","title": "Videogame Characters", "likes":50, "date": "2019-10-02",
        'description':'Recognize these iconic characters?',"question type": "OpenEnded", "questions" : entretainment_questions},
        {"id":"9","title": "Guess the Artist", "likes":100, "date": "2018-02-25",
        'description':'Can you match song titles to their respective artists',"question type": "OpenEnded", "questions" : entretainment_questions} ]


    cats = {'History': {'quizzes': history_quizzes, "id": 1, "description": "All but historical knowledge", "title": "History"},
            'Science': {'quizzes': science_quizzes, "id": 2,"description": "Test yourself against the sciences","title": "Science"},
            'Entretainment': {'quizzes': entretainment_quizzes, "id": 3, "description": "Think you know all abut entretainment","title": "Entretainment"} }
    

    

    for cat, cat_data in cats.items():
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        the_user.check_password("12345")
        the_user.check_password("12345")
        id = cat_data["id"]
        title = cat
        description = cat_data["description"]
        c = add_category(id,cat,description)
        for q in cat_data['quizzes']:
            quiz = add_quiz(c, q['id'], q['title'],the_user,q["date"],q["description"],q["question type"], q["likes"])
            quiz_id = q["id"]
            for question in q["questions"]:
                if question["quiz id"] == quiz_id and q["question type"] == "MultipleChoice":
                    the_question = add_multiple_choice(question["id"],quiz,question["image"],question["text"])
                    for choice in question["choices"]:
                        if choice["question id"] == question["id"]:
                            add_choice(choice["id"], the_question,choice["text"], choice["correct"])


                elif question["quiz id"] == quiz_id and q["question type"] == "OpenEnded":
                    for answer in answers:
                        if question["id"] == answer["question id"]:
                            the_answer = answer["answer"]

                    add_open_ended(question["id"],quiz,question["image"],question["text"], the_answer)

                elif question["quiz id"] == quiz_id and q["question type"] == "TrueOrFalse":
                    for answer in answers:
                        if question["id"] == answer["question id"]:
                            the_answer = answer["answer"]

                    add_true_false(question["id"],quiz,question["image"],question["text"], the_answer)

def add_question(id,quiz, image, text):
    
    qe = Question.objects.get_or_create(parameter=quiz, title=title)[0]
    qe.save()
    return qe

def add_multiple_choice(id,quiz, image, text):
    qe = MultipleChoice.objects.get_or_create(id = id, quiz=quiz, image=image,text = text)[0]
    qe.save()
    return qe

def add_choice(id,question, text, correct):
    ch = Choice.objects.get_or_create(id = id, question=question,text = text, correct = correct)[0]
    ch.save()
    return ch


def add_true_false(id,quiz, image, text, answer):
    qe = TrueOrFalse.objects.get_or_create(id = id, quiz=quiz, image=image,text = text, answer = answer)[0]
    qe.save()
    return qe

def add_open_ended(id,quiz, image, text, answer):
    qe = OpenEnded.objects.get_or_create(id = id, quiz=quiz, image=image,text = text, answer = answer)[0]
    qe.save()
    return qe

def add_quiz(cat,id,title,creator,date,description,QuestionType,likes):
    qi = Quiz.objects.get_or_create(category = cat, id=id,title=title, creator = creator,
    date = date,description=description,questionType=QuestionType,likes=likes)[0]
    qi.save()
    return qi

def add_category(id,title,description):
    c = Category.objects.get_or_create(id=id,title=title,description = description)[0]
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Quizker population script...')
    populate()