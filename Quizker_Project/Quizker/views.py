from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Quizker.forms import QuizForm,TrueOrFalseForm,QuestionTypeForm,OpenEndedForm,MultipleChoiceForm,ChoiceForm
from .models import Quiz,Question,Choice,MultipleChoice,TrueOrFalse,OpenEnded
from django.shortcuts import redirect,reverse
from django.urls import reverse 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.template.defaultfilters import slugify 

def Home(request):
    return render(request, 'Quizker/Home.html',context={})

def CreateTrueOrFalse(request, quiz_title_slug):
     if request.method == 'POST':
          form = TrueOrFalseForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
               return render(request, 'Quizker/TrueOrFalse.html',context={'form':TrueOrFalseForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
               
          else:
            print(form.errors)
        
     return render(request, 'Quizker/TrueOrFalse.html',context={'form':TrueOrFalseForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
def CreateOpenEnded(request, quiz_title_slug):
     if request.method == 'POST':
          form = OpenEndedForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
               return render(request, 'Quizker/OpenEnded.html',context={'form':OpenEndedForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)})
          else:
            print(form.errors)
     return render(request, 'Quizker/OpenEnded.html',context={'form':OpenEndedForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
def CreateMultipleChoice(request,quiz_title_slug):
     if request.method == 'POST':
          form = MultipleChoiceForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
               
               return redirect('/Quizker/Choice/'+str(Q.id)+'/')
          else:
            print(form.errors)
        
     return render(request, 'Quizker/MultipleChoice.html',context={'form':MultipleChoiceForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)})
def CreateChoice(request, question_id):
        if request.method == 'POST':
          form = ChoiceForm(request.POST)
          if form.is_valid():
               C = form.save(commit=False)
               C.question = Question.objects.get(id = int(question_id))
               C.save()
               numberOfChoice = Choice.objects.filter(question = C.question).count()
               if (numberOfChoice<4):
                   return render(request, 'Quizker/Choice.html',context={'form':ChoiceForm(),'Question':question_id})
               else:
                  url = '/Quizker/'+C.question.quiz.questionType+'/'+C.question.quiz.slug+'/'
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
              if qType == '2':
                  url = '/Quizker/TrueOrFalse/' + quiz_title_slug+'/'
                  return redirect(url)
              elif qType=='1':
                  url = '/Quizker/TrueOrFalse/' + quiz_title_slug+'/'
                  return redirect(reverse(url))
              elif qType=='3':
                  url = '/Quizker/TrueOrFalse/'+ quiz_title_slug+'/'
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
               url = '/Quizker/'+Quiz.questionType+'/'+Quiz.slug+'/'
               return redirect(url)
          else:
               print(form.errors)
        
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form})
def Quizzes(request):
     categories = Category.objects.all()
     context_dict = 'Quizzes'
     for category in categories:
         
def ParticipateQuiz(request, quiz_title_slug, question_number):
    
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    context_dict ={"QuestionNumber":question_number,"Quiz":quiz}
    quizType = quiz.questionType
    if (question_number < Question.objects.filter(quiz=quiz).count()):
     if (quizType=="TrueOrFalse"):
        QList = list(TrueOrFalse.objects.filter(quiz=quiz))
        context_dict['TrueOrFalse'] = True
        
     elif(quizType=="MultipleChoice"):
        QList = list(MultipleChoice.objects.filter(quiz=quiz))
        context_dict['Question'] = QList[question_number]
        context_dict['MultipleChoice'] = True
        context_dict['Choices'] = Choice.objects.filter(question = QList[question_number])
     else:
        QList = list(OpenEnded.objects.filter(quiz=quiz))
        context_dict['OpenEnded'] = True
    if request.method == "POST" :
          answeredQuestion = QList[question_number-1]
          answer = request.POST.get('answer', None)    
          if (quizType=="TrueOrFalse"):
              print(answer)
              print(answeredQuestion.correctAnswer(answer))
              
          elif(quizType=="MultipleChoice"):
               
              
              print(answer)
             
              
             
          if (question_number+1<len(QList)):
              question_number  += 1 
              return redirect('/Quizker/ParticipateQuiz/'+quiz.slug+'/'+str(question_number)+'/')
          else:
              return redirect('/Quizker/')
    context_dict['Question'] = QList[question_number]
    return render(request,'Quizker/ParticipateQuiz.html',context=context_dict)

