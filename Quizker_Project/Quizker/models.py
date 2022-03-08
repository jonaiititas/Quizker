from django.db import models
from django.template.defaultfilters import slugify 

# Create your models here.
class Category(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=128, unique=True)
        description = models.CharField(max_length=256)
        def __str__(self):
             return self.title 
        class Meta:
            verbose_name_plural = "Categories"
class Quiz(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length = 128,unique=True)
        #Creator = models.ForeignKey(User, on_delete=models.CASCADE)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        date = models.DateField()
        description = models.CharField(max_length=256)
        slug = models.SlugField(unique=True)
        def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Quiz,self).save(*args, **kwargs)
        def __str__(self):
             return self.title
        class Meta:
            verbose_name_plural = "Quizzes"
class Question(models.Model):
        id = models.AutoField(primary_key=True)
        quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
        image = models.ImageField(blank=True)
        max_length_text =256
        Text = models.CharField(max_length=max_length_text)
        def __str__(self):
             return self.Quiz.Title + " "+str(self.QuestionID)

class TrueOrFalse(Question):
        answer = models.BooleanField()
        def correctAnswer(self,attempt):
               return answer==attempt
        class Meta:
            verbose_name_plural = "True or False Questions"

class OpenEnded(Question):
        answer = models.CharField(max_length=128)
        def correctAnswer(self,attempt):
              return answer == attempt
        class Meta:
            verbose_name_plural = "Open ended Questions"

class MultipleChoice(Question):
       def correctAnswer(self,choice):
              return choice.correct
       class Meta:
            verbose_name_plural = "Multiple Choice Questions"
  
class Choice(models.Model):

        id = models.AutoField(primary_key=True)
        question = models.ForeignKey(MultipleChoice,on_delete=models.CASCADE)
        text = models.CharField(max_length=128)
        correct = models.BooleanField(default=False)
        def __str__(self):
            return str(self.choiceID)

