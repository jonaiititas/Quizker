from django.db import models


# Create your models here.
class Category(models.Model):
        Title = models.CharField(max_length=128, unique=True)
        Description = models.CharField(max_length=256)
        
class Quiz(models.Model):
        Title = models.CharField(max_length = 128,unique=True)
        #Creator = models.ForeignKey(User, on_delete=models.CASCADE)
        Category = models.ForeignKey(Category, on_delete=models.CASCADE)
        Date = models.DateField()
        Description = models.CharField(max_length=256)
class Question(models.Model):
        models.CharField(max_length =128)
        QuestionID = models.IntegerField()
        Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
        Image = models.ImageField()
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
              return choice.Correct
class choice(models.Model):
        ChoiceID = models.IntegerField()
        Question = models.ForeignKey(MultipleChoice,on_delete=models.CASCADE)
        Text = models.CharField(max_length=128)
        Correct = models.BooleanField(default=False)
       

