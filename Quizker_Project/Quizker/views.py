from django.shortcuts import render
from Quizker.forms import QuizForm
from .models import Quiz
# Create your views here.
def Home(request):
    return render(request, 'Quizker/Home.html',context={})
def CreateQuiz(request):
     form = QuizForm()
     if request.method == 'POST':
          form = QuizForm(request.POST)
          if form.is_valid():
               form.save(commit=True)
               return redirect('/Quizker/')
     else:
        print(form.errors)
        
     return render(request, 'Quizker/CreateQuiz.html',context={'form':form})
     
     





