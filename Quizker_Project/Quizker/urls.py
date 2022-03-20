from django.urls import path
from  Quizker import views

app_name  = 'Quizker'
urlpatterns = [
     path('',views.Home,name="Home"),
     path('CreateQuiz/',views.CreateQuiz,name='CreateQuiz'),
     path('CreateQuiz/CreateQuestion/<slug:quiz_title_slug>/',views.CreateQuestion,name="CreateQuestion"),
     path('CreateChoice/<int:question_id>/',views.CreateChoice,name='CreateChoice'),
     path('ParticipateQuiz/<slug:quiz_title_slug>/',views.ParticipateQuiz,name='ParticipateQuiz'),
     path('Results/<slug:quiz_title_slug>/',views.Results,name='Results'),
     
]

        