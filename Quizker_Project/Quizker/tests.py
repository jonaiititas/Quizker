from django.test import TestCase
from .models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice, QuizAttempt
from django.urls import reverse
import os
import warnings
import importlib
from Quizker.models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice, QuizAttempt
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

#Test Meta functions
class CategoryMethodTests(TestCase):
    def test_ensure_title_not_empty(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        self.assertEqual((category.title != ""), True)

    def correct_str_method

# Create your tests here.
class CategoryMethodTests(TestCase):
    print(squigames)

#for quiz attempt, points cant be negative, same as questions attempted
class Chapter5PopulationScriptTests(TestCase):

    """
    Tests whether the population script puts the expected data into a test database.
    All values that are explicitly mentioned in the book are tested.
    Expects that the population script has the populate() function, as per the book!
    """
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import populate_quizker
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}The Chapter 5 tests could not import the populate_rango. Check it's in the right location (the first tango_with_django_project directory).{FAILURE_FOOTER}")
        
        if 'populate' not in dir(populate_quizker):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the populate_rango module. This is required.{FAILURE_FOOTER}")
        
        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        populate_quizker.populate()