from django.urls import path
from  Quizker import views

app_name  = 'Quizker'
urlpatterns = [
     path('',views.Home,name="Home"),
     path('CreateQuiz/',views.CreateQuiz,name='CreateQuiz'),
     path('QuestionType/<slug:quiz_title_slug>/',views.QuestionType,name='QuestionType'),
     path('CreateQuestion/<slug:quiz_title_slug>/',views.TrueOrFalse,name='TrueOrFalse'),
     
]

        