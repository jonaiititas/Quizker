from django import forms
from Quizker.models import Category,Quiz,TrueOrFalse,OpenEnded,MultipleChoice,Choice,Question
import datetime
from django.template.defaultfilters import slugify

 
class QuizForm(forms.ModelForm):
     title=forms.CharField(max_length=256,help_text="Quiz name.")
     category = forms.ModelChoiceField(queryset=Category.objects.all())
     date = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today())
     description = forms.CharField(help_text = "A brief description of your quiz",max_length=256)
     slug = forms.SlugField(widget=forms.HiddenInput(),required=False)
     class Meta:
          model = Quiz
          fields=('title','category','description',)
          
class QuestionForm(forms.ModelForm):
     ID = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
     Text = forms.CharField(max_length=256,help_text="Question text")
     class Meta:
         model = Question 
         exclude= ('Quiz',)
         
class TrueOrFalseForm(QuestionForm):
     Answer = forms.BooleanField(help_text="True or False?")
     class Meta:
         model = TrueOrFalse
         exclude= ('Quiz',)
class OpenEndedForm(QuestionForm):
     Answer = forms.CharField(max_length=128,help_text="What is the answer?")
     class Meta:
         model = OpenEnded
         exclude= ('Quiz',)
class MultipleChoiceForm(QuestionForm):
     class Meta:
         model = MultipleChoice
         exclude= ('Quiz',)
class ChoiceForm(forms.ModelForm):
     ChoiceID = forms.IntegerField(initial=0)
     Text = forms.CharField(max_length=128,help_text="Choice Text")
     Correct = forms.BooleanField(initial=False)
     class Meta:
         model = Choice
         exclude = ('Question',)
class QuestionTypeForm(forms.ModelForm):
     Category = forms.CharField(help_text="What type of question?",widget=forms.Select(choices=['True or False','Open Ended','Multiple Choice']))
     




