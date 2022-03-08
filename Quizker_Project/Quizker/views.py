from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Quizker.forms import QuizForm,QuestionTypeForm,TrueOrFalseForm,OpenEndedForm,MultipleChoiceForm
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
def TrueOrFalse(request, quiz_title_slug):
    return HttpResponse("Hello")
def QuestionType(request,quiz_title_slug):
     form = QuestionType()
     if request.method =='POST':
         form = QuestionTypeForm(request.POST)
         if form.is_valid():
              qType = form.QuestionType
              if (qType == "True or False"):
                  return TrueOrFalse(request,quiz_title_slug)
              elif(qType=="Open Ended"):
                  return TrueOrFalse(request,quiz_title_slug)
              else:
                  return TrueOrFalse(request,quiz_title_slug)
         else:
             print(form.errors)
     return render(request, 'Quizker/QuestionType.html',context={'form':form})
        


def CreateQuiz(request):
     form = QuizForm()
     if request.method == 'POST':
          form = QuizForm(request.POST)
          if form.is_valid():
               Quiz = form.save(commit=False)
               Quiz.date = datetime.date.today()
               Quiz.save()
               return QuestionType(HttpRequest(), Quiz.slug)
     else:
        print(form.errors)
        
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form})




