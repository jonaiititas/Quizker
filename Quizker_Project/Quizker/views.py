from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Quizker.forms import QuizForm,TrueOrFalseForm,QuestionTypeForm,OpenEndedForm,MultipleChoiceForm,ChoiceForm
from .models import Quiz,Question,Choice,MultipleChoice
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
     if request.method == 'POST':
          form = TrueOrFalseForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
               url = '/Quizker/QuestionType/'+ Q.quiz.slug +'/'
               return redirect(url)
          else:
            print(form.errors)
        
     return render(request, 'Quizker/TrueOrFalse.html',context={'form':TrueOrFalseForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
def OpenEnded(request, quiz_title_slug):
     if request.method == 'POST':
          form = OpenEndedForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
               url = '/Quizker/QuestionType/'+ Q.quiz.slug +'/'
               return redirect(url)
          else:
            print(form.errors)
        
     return render(request, 'Quizker/TrueOrFalse.html',context={'form':OpenEndedForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
def MultipleChoice(request,quiz_title_slug):
     if request.method == 'POST':
          form = MultipleChoiceForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
               url = '/Quizker/Choice/'+ str(Q.id) +'/'
               return redirect(url)
          else:
            print(form.errors)
        
     return render(request, 'Quizker/MultipleChoice.html',context={'form':MultipleChoiceForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)})
def Choice(request, question_id):
        if request.method == 'POST':
          form = ChoiceForm(request.POST)
          if form.is_valid():
               C = form.save(commit=False)
               
               C.question = Question.objects.get(id = int(question_id))
               C.save()
               url = '/Quizker/QuestionType/'+ C.question.quiz.slug +'/'
               return redirect(url)
          else:
            print(form.errors)
        
        return render(request, 'Quizker/Choice.html',context={'form':ChoiceForm(),'Question':question_id})
 
def QuestionType(request,quiz_title_slug):
     if request.method =='POST':
         form = QuestionTypeForm(request.POST)
         if form.is_valid():
              model = form.save(commit=False)
              qType = model.QType
              if (qType == '2'):
                  url = '/Quizker/TrueOrFalse/' + quiz_title_slug+'/'
                  return redirect(url)
              elif(qType=='1'):
                  url = '/Quizker/OpenEnded/' + quiz_title_slug+'/'
                  return redirect(url)
              elif(qType=='3'):
                  url = '/Quizker/MultipleChoice/'+ quiz_title_slug+'/'
                  return redirect(url)
         else:
             print(form.errors)
     else:
          form = QuestionTypeForm()
          return render(request, 'Quizker/QuestionType.html',context={'form':form,'Quiz':Quiz.objects.get(slug=quiz_title_slug)})
        


def CreateQuiz(request):
     form = QuizForm()
     if request.method == 'POST':
          form = QuizForm(request.POST)
          if form.is_valid():
               Quiz = form.save(commit=False)
               Quiz.date = datetime.date.today()
               Quiz.save()
               url = '/Quizker/QuestionType/'+Quiz.slug+'/'
               return redirect(url)
     else:
        print(form.errors)
        
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form})




