import os
os.environ.setdefault('QUIZKER_SETTINGS_MODULE',
                'quizker_project.settings')

import django
django.setup()
from Quizker.models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice

def populate():















if __name__ == '__main__':
    print('Starting Quizker population script...')
    populate()