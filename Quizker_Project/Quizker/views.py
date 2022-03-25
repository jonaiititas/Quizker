from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Quizker.forms import QuizForm,TrueOrFalseForm,OpenEndedForm,MultipleChoiceForm,ChoiceForm
from .models import Quiz,Question,Choice,MultipleChoice,TrueOrFalse,OpenEnded,QuizAttempt,Category
from django.shortcuts import redirect,reverse
from django.urls import reverse 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.template.defaultfilters import slugify 
from django.views import View

def Home(request):
    return render(request, 'Quizker/Home.html',context={'Quizzes':Quiz.objects.all()[:5]})
@login_required
def CreateQuiz(request):
     form = QuizForm()
     if request.method == 'POST':
          form = QuizForm(request.POST)
          if form.is_valid():
               quiz = form.save(commit=False)
               quiz.date = datetime.date.today()
               quiz.creator = request.user
               quiz.likes = 0 
               quiz.save()
               return redirect(reverse("Quizker:CreateQuestion" ,kwargs={'quiz_title_slug':quiz.slug,}))
              
          else:
               print(form.errors)
          
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form,'numberofquizzes':((Quiz.objects.filter(creator=request.user).count())+1)})
@login_required
def CreateQuestion(request,quiz_title_slug):
          quiz = Quiz.objects.get(slug=quiz_title_slug)
          questionType = quiz.questionType
          print(questionType)
          if questionType=="OpenEnded":
             form = OpenEndedForm
          elif questionType =="TrueOrFalse":
             form = TrueOrFalseForm
          else: 
             form = MultipleChoiceForm
          if request.method == 'POST':
             completedForm = form(request.POST)
             if completedForm.is_valid():
               Q = completedForm.save(commit=False)
               Q.quiz = Quiz.objects.get(slug=quiz_title_slug)
               if 'image' in request.FILES:
                    Q.image = request.FILES['image']
               Q.save()
             if questionType=='MultipleChoice':
                return redirect(reverse('Quizker:CreateChoice',kwargs={'question_id':Q.id}))
             else:
               print(completedForm.errors)
        
          return render(request, 'Quizker/CreateQuestion.html',context={'form':form(),'Quiz':Quiz.objects.get(slug=quiz_title_slug)}) 
     
@login_required
def CreateChoice(request, question_id):
        if request.method == 'POST':
          form = ChoiceForm(request.POST)
          
          if form.is_valid():
               C = form.save(commit=False)
               
               C.question = Question.objects.get(id = int(question_id))
               C.save()
               numberOfChoices = Choice.objects.filter(question = C.question).count()
               
               if (numberOfChoices==4):           
                  return redirect(reverse('Quizker:CreateQuestion',kwargs={'quiz_title_slug':C.question.quiz.slug}))
          else:
               print(form.errors)
        
        return render(request, 'Quizker/CreateChoice.html',context={'form':ChoiceForm(),'Question':question_id})
 
def Quizzes(request):
    return render(request, 'Quizker/Quizzes.html',context={'Quizzes':Quiz.objects.all().order_by('-date')})

@login_required 
def ParticipateQuiz(request, quiz_title_slug):
    
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    quizAttempt = QuizAttempt.objects.get_or_create(quiz=quiz,user=request.user)[0]
    if (quizAttempt.questionsCompleted  == Question.objects.filter(quiz=quiz).count()):
                   return redirect(reverse('Quizker:Results',kwargs={'quiz_title_slug':quiz_title_slug}))    
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
                  correct =  answeredQuestion.answer ==True
              else:
                  correct =  answeredQuestion.answer == False
           elif (quizType=="MultipleChoice"):
              if (answer=="True"):
                  correct =  True
              else:
                  correct =  False
           else:
              correct = answeredQuestion.correctAnswer(answer)
           quizAttempt.questionsCompleted+=1
           quizAttempt.save()
           if correct: 
              quizAttempt = QuizAttempt.objects.get(quiz=quiz,user=request.user)
              quizAttempt.score += 1 
              quizAttempt.save()
              context_dict['correct'] = "Well done you got it right!"
           else:
              context_dict['correct'] = "Oh no, you got it wrong!!"
           if (quizAttempt.questionsCompleted  == Question.objects.filter(quiz=quiz).count()):
                   return redirect(reverse('Quizker:Results',kwargs={'quiz_title_slug':quiz_title_slug}))      
          
    if (quizType=="MultipleChoice"):
        context_dict['Choices'] = Choice.objects.filter(question = QList[quizAttempt.questionsCompleted]) 
    context_dict['Question'] = QList[quizAttempt.questionsCompleted]
    #if (context_dict['question'].image != null):
    #    context_dict['image'] =  context_dict['question'].image   
    
  
    return render(request,'Quizker/ParticipateQuiz.html',context=context_dict)
@login_required
def Results(request,quiz_title_slug):
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    quizAttempt = QuizAttempt.objects.get(quiz=quiz,user=request.user)
    context_dict ={}
    context_dict['NoQuestions'] = Question.objects.filter(quiz=quiz).count()
    context_dict['score'] = quizAttempt.score
    context_dict['quiz'] = quiz
  
    return render(request,'Quizker/Results.html',context_dict)
@login_required
def LikeQuiz(request , quiz_title_slug):
        if request.method=="POST":
          quiz = Quiz.objects.get(slug=quiz_title_slug)
          quizAttempt = QuizAttempt.objects.get(quiz=quiz,user=request.user)
          if (quizAttempt.liked ==False):
                 quiz.likes += 1 
                 quizAttempt.liked = True
          else:
                 quiz.likes -= 1  
                 quizAttempt.liked = False
                 
                
          quiz.save()     
          quizAttempt.save()
        return redirect(reverse('Quizker:Results',kwargs={'quiz_title_slug':quiz_title_slug})) 