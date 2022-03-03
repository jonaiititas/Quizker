from django.db import models


# Create your models here.
class Category(models.Model):
        Title = models.CharField(max_length=128, unique=True)
        Description = models.Charfield(max_length=256)
        
class Quiz(models.Model):
        Title = models.CharField(max_length = 128,unique=True)
        #Creator = models.ForeignKey(User, on_delete_cascade=True)
        Category = models.ForeignKey(Category, on_delete_cascade=True)
        Date = models.Date()
        Description = models.CharField(max_length=256)
class Question(models.Model):
        ID = models.IntegerField()
        Quiz = models.ForeignKey(Quiz, on_delete_cascade=True)
        Image = models.Image()
        Text = models.CharField(max_length=256)
class TrueOrFalse(Question):
        Answer = models.BooleanField()
        def correctAnswer(self,attempt):
               return Answer==attempt
class OpenEnded(Question):
        Answer = models.CharField(max_length=128)
        def correctAnswer(self,attempt):
              return Answer == attempt
class MultipleChoice(Question):
       def correctAnswer(self,choice):
              return choice.correct
class choice(models.Model):
        ID = models.IntegerField()
        Question = models.ForeignKey(MultipleChoice,on_delete_cascade=True)
        Text = models.CharField(max_length=128)
        Correct = models.BooleanField(default=False)
       

