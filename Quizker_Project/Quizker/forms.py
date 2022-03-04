from django import forms
from Quizker.models import Category,Quiz
import datetime
class QuizForm(forms.ModelForm):
     Title=forms.CharField(max_length=256,help_text="Quiz name.")
     Categories = Category.objects.all()
     Category = forms.ModelChoiceField(queryset=Category.objects.all())
     Date = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today())
     Description = forms.CharField(help_text = "A brief description of your quiz",max_length=256)
    
    

     
     
     
     
     
     
     
     
     







