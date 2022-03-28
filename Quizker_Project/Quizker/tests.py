from django.test import TestCase
from .models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice, QuizAttempt
from django.urls import reverse
import os
import warnings
import importlib
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from populate_quizker import populate

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

def add_quiz(cat,id,title,creator,date,description,QuestionType,likes= 0):
        quiz = Quiz.objects.get_or_create(category = cat, id=id,title=title, creator = creator,date = date,description=description,questionType=QuestionType,likes=likes)[0]
        quiz.save()
        return quiz


#Test Meta functions
class CategoryMethodTests(TestCase):
    def test_ensure_title_not_empty(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        self.assertEqual((category.title != ""), True)

class QuizMethodTests(TestCase):

    def test_ensure_id_unique(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        quiz = add_quiz(category,"01","Test Quiz",the_user,"2020-03-04","A lil test","OpenEnded",0)
        quiz.save()
        quiz2 = add_quiz(category,"01","Dummy Quiz",the_user,"2020-03-04","A lil testt","OpenEnded",0)
        quiz2.save()
        self.assertEqual((quiz.id != quiz2.id), True)
        print(quiz.id != quiz2.id)

    def test_quiz_starts_0_likes(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        quiz = add_quiz(category,"01","Test Quiz",the_user,"2020-03-04","A lil test","OpenEnded")
        self.assertEqual((quiz.likes == 0), True)

#class QuizMethodTests(TestCase):

class HomeViewTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('Quizker:Home'))
        self.content = self.response.content.decode()

    def test_home_message(self):

        response = self.client.get(reverse('Quizker:Home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A platform to take quizzes in a number of categories, compete with others and even create your own for a fun evening with your friends or school-work.')

    def test_template_filename(self):
        self.assertTemplateUsed(self.response, 'Quizker/Home.html', f"{FAILURE_HEADER}Wrong Template{FAILURE_FOOTER}")

class ContactUsViewTests(TestCase):
    
    def test_contact_us_message(self):

        response = self.client.get(reverse('Quizker:ContactUs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,

    def test_template_filename(self):
        self.assertTemplateUsed(self.response, 'Quizker/Home.html', f"{FAILURE_HEADER}Wrong Template{FAILURE_FOOTER}")

class QuizzesViewTests(TestCase):

    def set_up(self):
        self.response = self.client.get(reverse('Quizker:Quizzes'))
        self.content = self.response.content.decode()

    def test_quiz_existence(self):

        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        add_quiz(category,"01","Test Quiz",the_user,"2020-03-04","A lil test","OpenEnded",0)
        response = self.client.get(reverse('Quizker:Quizzes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Quiz")

    def test_quiz_order(self):

        expected_quiz_order = list(Quiz.objects.order_by('-date')[:5])
        self.assertTrue('Quizzes' in self.response.context, f"{FAILURE_HEADER}We couldn't find a 'categories' variable in the context dictionary within the index() view. Check the instructions in the book, and try again.{FAILURE_FOOTER}")
        self.assertEqual(type(self.response.context['Quizzes']), QuerySet, f"{FAILURE_HEADER}The 'categories' variable in the context dictionary for the index() view didn't return a QuerySet object as expected.{FAILURE_FOOTER}")
        self.assertEqual(expected_quiz_order, list(self.response.context['Quizzes']), f"{FAILURE_HEADER}Incorrect categories/category order returned from the index() view's context dictionary -- expected {expected_quiz_order}; got {list(self.response.context['Quizzes'])}.{FAILURE_FOOTER}")

class CreateQuizViewTests(TestCase):

    def proper_quiz_creation_message(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        add_quiz(category,"01","Test Quiz",the_user,"2020-03-04","A lil test","OpenEnded",0)
        response = self.client.get(reverse('CreateQuestion'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Congratulations, for you that is quiz number")

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