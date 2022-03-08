from django.db import models


# Create your models here.
class Category(models.Model):
        Title = models.CharField(max_length=128, unique=True)
        Description = models.CharField(max_length=256)
        def __str__(self):
             return self.Title 
        class Meta:
            verbose_name_plural = "Categories"

class Quiz(models.Model):
        Title = models.CharField(max_length = 128,unique=True)
        #Creator = models.ForeignKey(User, on_delete=models.CASCADE)
        Category = models.ForeignKey(Category, on_delete=models.CASCADE)
        Date = models.DateField()
        Description = models.CharField(max_length=256)
        def __str__(self):
             return self.Title
        class Meta:
            verbose_name_plural = "Quizzes"

class Question(models.Model):
        QuestionID = models.IntegerField(unique=True)
        Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
        Image = models.ImageField(blank=True)
        max_length_text =256
        Text = models.CharField(max_length=max_length_text)
        QID = 0
        def __str__(self):
             return self.Quiz.Title + " "+str(self.QuestionID)

class TrueOrFalse(Question):
        Answer = models.BooleanField()
        def correctAnswer(self,attempt):
               return Answer==attempt
        class Meta:
            verbose_name_plural = "True or False Questions"

class OpenEnded(Question):
        Answer = models.CharField(max_length=128)
        def correctAnswer(self,attempt):
              return Answer == attempt
        class Meta:
            verbose_name_plural = "Open ended Questions"

class MultipleChoice(Question):
       def correctAnswer(self,choice):
              return choice.Correct
       class Meta:
            verbose_name_plural = "Multiple Choice Questions"
  
class Choice(models.Model):
        ChoiceID = models.IntegerField(unique=True)
        Question = models.ForeignKey(MultipleChoice,on_delete=models.CASCADE)
        Text = models.CharField(max_length=128)
        Correct = models.BooleanField(default=False)
        CIQ=0
        def __str__(self):
            return self.Question.Quiz.Title + " "+str(self.Question.QuestionID) + " Choice " +str(self.ChoiceID)

