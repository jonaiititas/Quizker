from django.urls import path
from  Quizker import views

app_name  = 'Quizker'
urlpatterns = [
     path('',views.Home,name="Home"),
     path('CreateQuiz/',views.CreateQuiz,name='CreateQuiz'),
]

        