from django.urls import path
from  Quizker import views

app_name  = 'Quizker'
urlpatterns = [
     path('',views.Home,name="Home"),
     path('CreateQuiz/',views.CreateQuiz,name='CreateQuiz'),
     path('TrueOrFalse/<slug:quiz_title_slug>/',views.CreateTrueOrFalse,name='TrueOrFalse'),
     path('OpenEnded/<slug:quiz_title_slug>/',views.CreateOpenEnded,name='OpenEnded'),
     path('MultipleChoice/<slug:quiz_title_slug>/',views.CreateMultipleChoice,name='MultipleChoice'),
     path('Choice/<int:question_id>/',views.CreateChoice,name='Choice'),
     path('ParticipateQuiz/<slug:quiz_title_slug>/',views.ParticipateQuiz,name='ParticipateQuiz'),
     path('Results/<slug:quiz_title_slug>/',views.Results,name='Results'),
]

        