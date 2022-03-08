from django.shortcuts import render
from Quizker.forms import QuizForm,QuestionTypeForm
from .models import Quiz
from django.shortcuts import redirect,reverse
from django.urls import reverse 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.template.defaultfilters import slugify 
# Create your views here.
def Home(request):
    return render(request, 'Quizker/Home.html',context={})
def CreateQuiz(request):
     form = QuizForm()
     if request.method == 'POST':
          form = QuizForm(request.POST)
          if form.is_valid():
               Quiz = form.save(commit=False)
               Quiz.date = datetime.date.today()
               Quiz.save()
               form = QuestionTypeForm()
               return render(request,'/Quizker/QuestionType.html',context={'form':form,'Quiz':Quiz})
     else:
        print(form.errors)
        
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form})
def QuestionType(request, Quiz_name_slug):
     Quiz = Quiz.object.get(slug= Quiz_name_slug)
     form = QuestionType()
     if request.method =='POST':
         form = QuestionTypeForm(request.POST)
         if form.is_valid():
              print("hello")
              #qType = form.QuestionType
              #if (qType == "True or False"):
              #    return render(
              #else if(qType=="Open Ended"):
              #    return render(
              #else:
              #    return multipleChoice
         else:
             print(form.errors)
     return render(request, 'Quizker/QuestionType.html',context={'form':form,'Quiz':Quiz})




