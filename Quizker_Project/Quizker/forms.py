from django import forms
from Quizker.models import Category,Quiz,TrueOrFalse,OpenEnded,MultipleChoice,Choice,Question,QuestionType
import datetime
from django.template.defaultfilters import slugify
class QuizForm(forms.ModelForm):
     title=forms.CharField(max_length=256,help_text="Quiz name")
     category = forms.ModelChoiceField(queryset=Category.objects.all())
     date = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today())
     description = forms.CharField(help_text = "A brief description of your quiz",max_length=256)
     slug = forms.SlugField(widget=forms.HiddenInput(),required=False)
     questionType = forms.ChoiceField(help_text="What type of question?",choices =(('OpenEnded',"Open Ended"),('TrueOrFalse',"True or False"),('MultipleChoice',"Multiple Choice")))
     class Meta:
          model = Quiz
          fields=('title','category','description','questionType')
          
class QuestionForm(forms.ModelForm):
     text = forms.CharField(max_length=256,help_text="Question text")
     image = forms.ImageField(required=False)
     class Meta:
         model = TrueOrFalse
         fields=("text","image",)
         
class TrueOrFalseForm(QuestionForm):
     answer = forms.BooleanField(help_text="True or False?",required=False)
     class Meta:
         model = TrueOrFalse
         fields=("text","image","answer",)
class OpenEndedForm(QuestionForm):
     answer = forms.CharField(max_length=128,help_text="What is the answer?")
     class Meta:
         model = OpenEnded
         fields=("text","image","answer",)
class MultipleChoiceForm(QuestionForm):
     class Meta:
         model = MultipleChoice
         fields=("text","image",)
class ChoiceForm(forms.ModelForm):
     text = forms.CharField(max_length=128,help_text="Choice Text")
     correct = forms.BooleanField(required=False)
     class Meta:
         model = Choice
         fields = ('text','correct',)

class QuestionTypeForm(forms.ModelForm):
     QType = forms.ChoiceField(help_text="What type of question?",choices =(('1',"Open Ended"),('2',"True or False"),('3',"Multiple Choice")))
     class Meta:
          model = QuestionType
          fields= ('QType',)
          




