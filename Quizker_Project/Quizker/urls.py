from django.urls import path
from  Quizker import views

app_name  = 'Quizker'
urlpatterns = [
     path('',views.Home,name="Home"),
     path('CreateQuiz/',views.CreateQuiz,name='CreateQuiz'),
     path('QuestionType/<slug:quiz_title_slug>/',views.QuestionType,name='QuestionType'),
     path('TrueOrFalse/<slug:quiz_title_slug>/',views.CreateTrueOrFalse,name='TrueOrFalse'),
     path('OpenEnded/<slug:quiz_title_slug>/',views.CreateOpenEnded,name='OpenEnded'),
     path('MultipleChoice/<slug:quiz_title_slug>/',views.CreateMultipleChoice,name='MultipleChoice'),
     path('Choice/<str:question_id>/',views.CreateChoice,name='Choice'),
     path('ParticipateQuiz/<slug:quiz_title_slug>/<int:question_number>/',views.ParticipateQuiz,name='ParticipateQuiz'),
     
     
]

        