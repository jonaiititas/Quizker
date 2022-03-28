from django.db import models
from django.template.defaultfilters import slugify 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    questionType = models.CharField(max_length=64,choices =(('OpenEnded',"Open Ended"),('TrueOrFalse',"True or False"),('MultipleChoice',"Multiple Choice")))
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Quiz,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"

class QuizAttempt(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    questionsCompleted = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)
          
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Question_Images',blank=True)
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.quiz.title + " "+str(self.id)

class TrueOrFalse(Question):
    answer = models.BooleanField(blank=True)

    def correctAnswer(self,attempt):
        return self.answer == attempt

    class Meta:
        verbose_name_plural = "True or False Questions"

class OpenEnded(Question):
    answer = models.CharField(max_length=128)

    def correctAnswer(self,attempt):
        return self.answer == attempt
        
    class Meta:
        verbose_name_plural = "Open ended Questions"

class MultipleChoice(Question):
    def correct(self):
        choices = Choice.objects.filter(question=self)
        correct = False
        for choice in choices:
            if choice.correct == True:
                correct = True
        return correct 
            
    class Meta:
        verbose_name_plural = "Multiple Choice Questions"
  
class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(MultipleChoice,on_delete=models.CASCADE)
    text = models.CharField(max_length=128)
    correct = models.BooleanField(blank=True)
    def __str__(self):
        return str(self.id)

