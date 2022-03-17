from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Quizker.forms import QuizForm,TrueOrFalseForm,OpenEndedForm,MultipleChoiceForm,ChoiceForm
from .models import Quiz,Question,Choice,MultipleChoice,TrueOrFalse,OpenEnded,QuizAttempt
from django.shortcuts import redirect,reverse
from django.urls import reverse 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.template.defaultfilters import slugify 

def Home(request):
    
    return render(request, 'Quizker/Home.html',context={'Quizzes':Quiz.objects.all()})
def CreateQuiz(request):
     form = QuizForm()
     if request.method == 'POST':
          form = QuizForm(request.POST)
          if form.is_valid():
               Quiz = form.save(commit=False)
               Quiz.date = datetime.date.today()
               Quiz.creator = request.user
               Quiz.save()
               #return redirect(reverse(('Create'+Quiz.questionType),kwargs=('quiz_title_slug':Quiz.slug,)))
               url = '/Quizker/'+Quiz.questionType+'/'+Quiz.slug+'/'
               return redirect(url)
          else:
               print(form.errors)
        
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form})
def CreateTrueOrFalse(request, quiz_title_slug):
     if request.method == 'POST':
          form = TrueOrFalseForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
          else:
            print(form.errors)
        
     return render(request, 'Quizker/TrueOrFalse.html',context={'form':TrueOrFalseForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
def CreateOpenEnded(request, quiz_title_slug):
     if request.method == 'POST':
          form = OpenEndedForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.image = form.cleaned_data.get("image")
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
          else:
            print(form.errors)
     return render(request, 'Quizker/OpenEnded.html',context={'form':OpenEndedForm(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
def CreateMultipleChoice(request,quiz_title_slug):
     if request.method == 'POST':
          form = MultipleChoiceForm(request.POST)
          if form.is_valid():
               Q = form.save(commit=False)
               Q.image = form.cleaned_data.get("image")
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               Q.save()
               #return redirect(reverse('CreateChoice',args=(Q.id,)))
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
               print(numberOfChoices)
               if (numberOfChoice<4):
                   return render(request, 'Quizker/Choice.html',context={'form':ChoiceForm(),'Question':question_id})
               else:
                  #return redirect(reverse('CreateMultipleChioce',kwargs=('quiz_title_slug':C.question.quiz.slug,)))
                  url = '/Quizker/'+C.question.quiz.questionType+'/'+C.question.quiz.slug+'/'
                  return redirect(url)
          else:
               print(form.errors)
        
        return render(request, 'Quizker/Choice.html',context={'form':ChoiceForm(),'Question':question_id})
 

#def Quizzes(request):
#     categories = list(Category.objects.all())
#     context_dict={'categories':[]}
#     for category in categories:
#         context_dict[category.title] = list(Quiz.objects.filter(category=category)
#         context_dict['categories'].append(category.title)
     
     #return render(request, 'Quizker/Quizzes.html',context_dict)
     
def ParticipateQuiz(request, quiz_title_slug):
    
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    quizAttempt = QuizAttempt.objects.get_or_create(quiz=quiz,user=request.user)[0]
    if (quizAttempt.questionsCompleted  == Question.objects.filter(quiz=quiz).count()):
                   return redirect('/Quizker/Results/'+quiz_title_slug+'/')     
    context_dict ={"Quiz":quiz}
    quizType = quiz.questionType
    
    if (quizType=="TrueOrFalse"):
        QList = list(TrueOrFalse.objects.filter(quiz=quiz))
    elif(quizType=="MultipleChoice"):
        QList = list(MultipleChoice.objects.filter(quiz=quiz))
    else:
        QList = list(OpenEnded.objects.filter(quiz=quiz))
    context_dict[quizType] = True    
    if request.method == "POST" :
          answeredQuestion = QList[quizAttempt.questionsCompleted]
          answer = request.POST.get('answer', None) 
          if answer!=None:          
           
           if (quizType=="TrueOrFalse"):
              if (answer=="True"):
                  correct =  answeredQuestion.correctAnswer(True)
              else:
                  correct =  answeredQuestion.correctAnswer(False)
           if (quizType=="MultipleChoice"):
              if (answer=="True"):
                  correct =  True
              else:
                  correct =  False
           else:
              correct = answeredQuestion.correctAnswer(answer)
           quizAttempt.questionsCompleted+=1
           quizAttempt.save()
           if correct: 
              quizAttempt.score += 1 
              quizAttempt.save()
           if (quizAttempt.questionsCompleted  == Question.objects.filter(quiz=quiz).count()):
                   return redirect('/Quizker/Results/'+quiz_title_slug+'/')         
          
    if (quizType=="MultipleChoice"):
        context_dict['Choices'] = Choice.objects.filter(question = QList[quizAttempt.questionsCompleted])      
    context_dict['Question'] = QList[quizAttempt.questionsCompleted]
  
    return render(request,'Quizker/ParticipateQuiz.html',context=context_dict)

def Results(request,quiz_title_slug):
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    quizAttempt = QuizAttempt.objects.get(quiz=quiz,user=request.user)
    context_dict ={}
    context_dict['NoQuestions'] = Question.objects.filter(quiz=quiz).count()
    print(context_dict['NoQuestions'])
    context_dict['score'] = quizAttempt.score
    return render(request,'Quizker/Results.html',context_dict)