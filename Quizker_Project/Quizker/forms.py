from django import forms
from Quizker.models import Category,Quiz,TrueOrFalse,OpenEnded,MultipleChoice,choice,Question
import datetime
class QuizForm(forms.ModelForm):
     Title=forms.CharField(max_length=256,help_text="Quiz name.")
     Categories = Category.objects.all()
     Category = forms.ModelChoiceField(queryset=Category.objects.all())
     Date = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today())
     Description = forms.CharField(help_text = "A brief description of your quiz",max_length=256)
     class Meta:
          model = Quiz
          fields=('Title','Category','Date','Description',)
          
class QuestionForm(forms.ModelForm):
     ID = forms.IntegerField(widget=forms.HiddenInput(),initial=Question.QID)
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
     ChoiceID = forms.IntegerField(initial=choice.CIQ)
     Text = forms.CharField(max_length=128,help_text="Choice Text")
     Correct = forms.BooleanField(initial=False)
     class Meta:
         model = choice
         exclude = ('Question',)







