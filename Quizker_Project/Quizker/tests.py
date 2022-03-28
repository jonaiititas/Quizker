from django.test import TestCase
from .models import Category, Quiz, Question, TrueOrFalse, OpenEnded, MultipleChoice, Choice, QuizAttempt
from django.urls import reverse,path
import os
import warnings
import importlib
from .views import *
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

def add_open_ended(id,quiz, image, text, answer):
    qe = OpenEnded.objects.get_or_create(id = id, quiz=quiz, image=image,text = text, answer = answer)[0]
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

#Test Meta functions
class CategoryMethodTests(TestCase):
    def test_ensure_title_not_empty(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        self.assertEqual((category.title != ""), True)

class QuizMethodTests(TestCase):

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
        self.assertContains(response,"First Name")
        self.assertContains(response,"Last Name")
        self.assertContains(response,"Subject")

    def test_template_filename(self):
        response = self.client.get(reverse('Quizker:ContactUs'))
        self.assertTemplateUsed(response, 'Quizker/ContactUs.html', f"{FAILURE_HEADER}Wrong Template{FAILURE_FOOTER}")

class QuizzesViewTests(TestCase):

    def setUp(self):
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
        self.assertTrue('Quizzes' in self.response.context, )
        self.assertEqual(type(self.response.context['Quizzes']), QuerySet, )
        self.assertEqual(expected_quiz_order, list(self.response.context['Quizzes'])
    
    def test_template_filename(self):
        response = self.client.get(reverse('Quizker:Quizzes'))
        self.assertTemplateUsed(response, 'Quizker/Quizzes.html', f"{FAILURE_HEADER}Wrong Template{FAILURE_FOOTER}")

class CreateQuizViewTests(TestCase):
    

    def proper_quiz_creation_message(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        add_quiz(category,"10","Test Quiz 2",the_user,"2020-03-04","please work","OpenEnded",0)
        response = self.client.get(reverse('CreateQuestion'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Congratulations, for you that is quiz number")

    

#for quiz attempt, points cant be negative, same as questions attempted
class CreateQuestionViewTests(TestCase):


    def remove_question_existence(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        add_quiz(category,"15","Test Quiz 3",the_user,"2020-03-04","A lil test","OpenEnded",0)
        response = self.client.get(reverse('Quizker:CreateQuestion'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Remove")

    def test_question_existence(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        the_quiz = add_quiz(category,"07","Test Multiple Choice Quiz",the_user,"2020-04-03","Multiple Save","MultipleChoice",0)
        add_multiple_choice("01",the_quiz,None,"Which of this is a birb")
        response = self.client.get(reverse("Quizker:CreateQuestion",kwargs={"quiz_title_slug" : the_quiz.slug}))
        self.assertContains(response, "Which of this is a birb")

class CreateChoiceViewTests(TestCase):


    def test_choice_existence(self):
        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        the_quiz = add_quiz(category,"07","Test Multiple Choice Quiz",the_user,"2020-04-03","A lil test","MultipleChoice",0)
        the_question = add_multiple_choice("01",the_quiz,None,"Which of this is a birb")
        add_choice("01",the_question,"Dog",False)
        add_choice("02",the_question,"Cat",False)
        add_choice("03",the_question,"Eagle",True)
        response = self.client.get(reverse("Quizker:CreateChoice"))
        self.assertContains(response, "Dog")
        self.assertContains(response, "Cat")
        self.assertContains(response, "Eagle")

    #def test_template_filename(self):
        #response = self.client.get(reverse('Quizker:CreateChoice'))
        #self.assertTemplateUsed(response, 'Quizker/CreateChoice.html', f"{FAILURE_HEADER}Wrong Template{FAILURE_FOOTER}")

class ResultsViewTests(TestCase):
    def test_result_message(self):

        category = Category(id='01', title="", description ="Teste stuff eh")
        category.save()
        the_user = User.objects.get_or_create(username="Za Warudo", password = 0)[0]
        the_user.set_password("1234")
        the_quiz = add_quiz(category,"17","Test Multiple Choice Quiz 23",the_user,"2020-04-03","A lil test","MultipleChoice",0)
        response = self.client.get(reverse('Quizker:Results'),kwargs={"quiz_title_slug" : the_quiz.slug})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Congratulations, your result is')

class UserProfileViewTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('Quizker:UserProfile'))
        self.content = self.response.content.decode()

    def test_user_message(self):

        response = self.client.get(reverse('Quizker:UserProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Quizzes created")

    def test_template_filename(self):
        self.assertTemplateUsed(self.response, 'Quizker/UserProfile.html', f"{FAILURE_HEADER}Wrong Template{FAILURE_FOOTER}")

class LeadearboardViewTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('Quizker:Leaderboard'))
        self.content = self.response.content.decode()

    #def test_user_message(self):

        #response = self.client.get(reverse('Quizker:Home'))
        #self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'A platform to take quizzes in a number of categories, compete with others and even create your own for a fun evening with your friends or school-work.')

    def test_template_filename(self):
        self.assertTemplateUsed(self.response, 'Quizker/Leaderboard.html', f"{FAILURE_HEADER}Wrong Template{FAILURE_FOOTER}")


class Chapter5PopulationScriptTests(TestCase):

    def setUp(self):
        try:
            import populate_quizker
        except ImportError:
            raise ImportError
        
        if 'populate' not in dir(populate_quizker):
            raise NameError
        
        
        populate_quizker.populate()