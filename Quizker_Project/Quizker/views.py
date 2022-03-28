from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Quizker.forms import QuizForm,TrueOrFalseForm,OpenEndedForm,MultipleChoiceForm,ChoiceForm
from .models import Quiz,Question,Choice,MultipleChoice,TrueOrFalse,OpenEnded,QuizAttempt,Category,User
from django.shortcuts import redirect,reverse
from django.urls import reverse 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.template.defaultfilters import slugify 
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

def Home(request):
    return render(request, 'Quizker/Home.html',context={'Quizzes':Quiz.objects.all().order_by('-likes')[:5]})

@login_required
def CreateQuiz(request):

     form = QuizForm()
     user = request.user
     if request.method == 'POST':
          form = QuizForm(request.POST)
          if form.is_valid():
               #Adding the HiddenInput values 
               quiz = form.save(commit=False)
               quiz.date = datetime.date.today()
               quiz.creator = request.user
               quiz.likes = 0 
               quiz.save()
               #Directing the user to the create question page 
               return redirect(reverse("Quizker:CreateQuestion" ,kwargs={'quiz_title_slug':quiz.slug,}))
              
          else:
               print(form.errors)
      
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form,'numberofquizzes':((Quiz.objects.filter(creator=request.user).count())+1)})

@login_required
def CreateQuestion(request,quiz_title_slug):
          quiz = Quiz.objects.get(slug=quiz_title_slug)
          #Checking if the user is the creator 
          if quiz.creator!=request.user:
               return redirect('/Quizker/')
          #Determing what questionType the quiz has 
          questionType = quiz.questionType
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
               #checking if the question is multiple choice if so it redirects to the create choices page 
               if questionType=='MultipleChoice':
                  return redirect(reverse('Quizker:CreateChoice',kwargs={'question_id':Q.id}))
             else:
               print(completedForm.errors)
        
          return render(request, 'Quizker/CreateQuestion.html',context={'form':form(),'Quiz':quiz,'Questions':Question.objects.filter(quiz=quiz)}) 
     
@login_required
def CreateChoice(request, question_id):
        
        if request.method == 'POST':
          form = ChoiceForm(request.POST)
          
          
          if form.is_valid():
               C = form.save(commit=False)
               C.question = MultipleChoice.objects.get(id = int(question_id))
               if C.question.correct():
                  C.correct = False
               C.save()
          else:
               print(form.errors)
        context_dict ={}
        context_dict['Choices'] = Choice.objects.filter(question=MultipleChoice.objects.get(id=question_id))
        context_dict['question'] = MultipleChoice.objects.get(id=question_id)
        context_dict['form'] = ChoiceForm()
        return render(request, 'Quizker/CreateChoice.html',context_dict)
 
def Quizzes(request):

    return render(request, 'Quizker/Quizzes.html',context={'Quizzes':Quiz.objects.all().order_by('-date')})

@login_required 
def ParticipateQuiz(request, quiz_title_slug):
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    #Checking if Quiz has any questions if it does not then it is deleted and user is redirected to Home Page
    if Question.objects.filter(quiz=quiz).count()==0:
       Quiz.objects.get(slug=quiz_title_slug).delete()
       return redirect('/Quizker/')
    quizAttempt = QuizAttempt.objects.get_or_create(quiz=quiz,user=request.user)[0]
    #checking if user has completed the quiz if it has then it is directed to results page 
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
          #Extracting answer 
          answer = request.POST.get('answer', None)  
          #Checking if answer has a value 
          if answer!=None:          
           #Checking which question it is and checking the answer accordingly 
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
           #Iterating through the question 
           quizAttempt.questionsCompleted+=1
           quizAttempt.save()
           if correct: 
              #if answer is correct then one is added to the score 
              quizAttempt = QuizAttempt.objects.get(quiz=quiz,user=request.user)
              quizAttempt.score += 1 
              quizAttempt.save()
              #adding javascript alert message 
              context_dict['correct'] = "Well done you got it right!"
           else:
              #Adding javascipt alert message
              context_dict['correct'] = "Oh no, you got it wrong!!"
    #If MultipleChoice then choies are added               
    if (quizType=="MultipleChoice"):
        context_dict['Choices'] = Choice.objects.filter(question = QList[quizAttempt.questionsCompleted]) 
    context_dict['Question'] = QList[quizAttempt.questionsCompleted]
    context_dict['quizAttempt'] = quizAttempt
    context_dict['QuestionNumber'] = quizAttempt.questionsCompleted + 1 

    
  
    return render(request,'Quizker/ParticipateQuiz.html',context=context_dict)

@login_required
def Results(request,quiz_title_slug):
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    quizAttempt = QuizAttempt.objects.get(quiz=quiz,user=request.user)

    context_dict ={}
    context_dict['NoQuestions'] = Question.objects.filter(quiz=quiz).count()
    context_dict['score'] = quizAttempt.score
    context_dict['quiz'] = quiz
    context_dict['QuizAttempts'] = QuizAttempt.objects.filter(quiz=quiz).order_by('-score')[:5]
    return render(request,'Quizker/Results.html',context_dict)

@login_required
def FinishQuiz(request,quiz_title_slug):
    quiz = Quiz.objects.get(slug=quiz_title_slug)
    #Checking if quiz has any question if it does not then quiz is deleted
    if Question.objects.filter(quiz=quiz).count()==0:
        Quiz.objects.get(slug=quiz_title_slug).delete()
    return redirect('/Quizker/')

@login_required          
def RemoveQuestion(request, quiz_id):
   
    quiz = Question.objects.get(id=quiz_id).quiz
    #Checking if user is the creator of the quiz 
    if quiz.creator!=request.user:
        return redirect('/Quizker/')
    Question.objects.get(id=quiz_id).delete()   
    return redirect(reverse("Quizker:CreateQuestion" ,kwargs={'quiz_title_slug':quiz.slug,}))

@login_required          
def RemoveChoice(request, choice_id):
    question = Choice.objects.get(id=choice_id).question
    #Checking if the user is  the creator of the quiz 
    if question.quiz.creator!=request.user:
        return redirect('/Quizker/')
    Choice.objects.get(id=choice_id).delete()   
    return redirect(reverse("Quizker:CreateChoice" ,kwargs={'question_id':question.id,}))

@login_required
def AddChoices(request, question_id):
    question = MultipleChoice.objects.get(id=question_id)
    #Checking if the user is  the creator of the quiz 
    if question.quiz.creator!=request.user:
        return redirect('/Quizker/')
    #Checking if there are more than 1 choice 
    if Choice.objects.filter(question=question).count()<2:
       return redirect(reverse("Quizker:CreateChoice" ,kwargs={'question_id':question_id,}))
    #Checking if there is a true Choice
    if question.correct()==False:
        MultipleChoice.objects.get(id=question_id).delete()
    return redirect(reverse("Quizker:CreateQuestion" ,kwargs={'quiz_title_slug':question.quiz.slug,}))

@login_required
def LikeQuiz(request , quiz_title_slug):
        if request.method=="POST":
          quiz = Quiz.objects.get(slug=quiz_title_slug)
          quizAttempt = QuizAttempt.objects.get(quiz=quiz,user=request.user)
          #Liking and unliking the quiz accordingly
          if (quizAttempt.liked ==False):
                 quiz.likes += 1 
                 quizAttempt.liked = True
          else:
                 quiz.likes -= 1  
                 quizAttempt.liked = False

          quiz.save()     
          quizAttempt.save()
        return redirect(reverse('Quizker:Results',kwargs={'quiz_title_slug':quiz_title_slug}))

@login_required
def UserProfile(request):
    user = request.user
    context_dict = {}
    context_dict['Quizzes'] = Quiz.objects.filter(creator=user).order_by('-date')
    context_dict['User'] = user
    context_dict['QuizzesCreated'] = Quiz.objects.filter(creator=request.user).count()
    context_dict['QuizzesCompleted'] = QuizAttempt.objects.filter(user=request.user).count()
    context_dict['QuizzesLiked'] = 0 
    #Iterating through each QuizAttempt checking if it's a liked question and if it's a completed quiz 
    for quizAttempt in QuizAttempt.objects.filter(user=request.user):
          if quizAttempt.liked:
              context_dict['QuizzesLiked'] += 1 
          if quizAttempt.questionsCompleted != Question.objects.filter(quiz=quizAttempt.quiz).count():
             context_dict['QuizzesCompleted'] -= 1 
    return render(request, 'Quizker/UserProfile.html',context=context_dict)

def Leaderboard(request):
    users = []
    #creating an instance for each user getting their overall percentage success rate for the quizzes 
    for user in User.objects.all():
        score = 0
        QuizzesIncomplete = 0
        Quizzes = QuizAttempt.objects.filter(user=user)
        for quizAttempt in Quizzes:
            if quizAttempt.questionsCompleted!=Question.objects.filter(quiz=quizAttempt.quiz).count():
               QuizzesIncomplete +=1 
            else:
               score += (quizAttempt.score/Question.objects.filter(quiz=quizAttempt.quiz).count())*100
        if Quizzes.count()!=0:
           users.append([user.username,round(score/(Quizzes.count()-QuizzesIncomplete),1),(Quizzes.count()-QuizzesIncomplete)])
    users = sorted(users,key=lambda x:x[1],reverse=True)    
    return render(request, 'Quizker/Leaderboard.html',context={'Users':users})

def ContactUs(request):
    return render(request, 'Quizker/ContactUs.html')