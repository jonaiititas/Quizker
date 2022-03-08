import os
os.environ.setdefault('QUIZKER_SETTINGS_MODULE',
                'quizker_project.settings')

import django
django.setup()
from Quizker.models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice

def populate():
    #ola Peter
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',"views": 8},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',"views": 10},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',"views": 30} ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',"views": 24},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',"views": 13},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',"views": 25}]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',"views": 15},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',"views": 5} ]

    quizz = {'Python': {'pages': python_pages, "likes": 64, "views": 128},
            'Django': {'pages': django_pages, "likes": 32, "views": 64},
            'Other Frameworks': {'pages': other_pages, "likes": 16, "views": 32} }
    
    #print("a")

def add_question(quiz, title, url, views=0):
    #Chech get_or_create inputs to properly calll function
    qe = Question.objects.get_or_create(parameter=quiz, title=title)[0]
    qe.url=url
    qe.views=views
    qe.save()
    return qe

def add_quiz(name,views,likes):
    qi = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    qi.save()
    return qi

















if __name__ == '__main__':
    print('Starting Quizker population script...')
    populate()