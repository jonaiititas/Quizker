from django.urls import path
from Quizker import views

app_name  = 'Quizker'
urlpatterns = [
     path('',views.Home,name="Home"),
     path('AllQuizzes/',views.Quizzes,name='Quizzes'),
     path('CreateQuiz/',views.CreateQuiz,name='CreateQuiz'),
     path('CreateQuiz/CreateQuestion/<slug:quiz_title_slug>/',views.CreateQuestion,name="CreateQuestion"),
     path('CreateQuiz/CreateQuestion/CreateChoice/<int:question_id>/',views.CreateChoice,name='CreateChoice'),
     path('ParticipateQuiz/<slug:quiz_title_slug>/',views.ParticipateQuiz,name='ParticipateQuiz'),
     path('Results/<slug:quiz_title_slug>/',views.Results,name='Results'),
     path('like_quiz/<slug:quiz_title_slug>/', views.LikeQuiz, name='like_quiz'),
     path('CreateQuiz/FinishQuiz/<slug:quiz_title_slug>/',views.FinishQuiz,name='FinishQuiz'),
     path('CreateQuiz/RemoveQuestion/<int:quiz_id>/',views.RemoveQuestion,name='RemoveQuestion'),
     path('CreateQuiz/CreateQuestion/RemoveChoice/<int:choice_id>/',views.RemoveChoice,name='RemoveChoice'),
]

        