from django.contrib import admin
from Quizker.models import Category,Quiz,TrueOrFalse,OpenEnded,MultipleChoice,choice

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(TrueOrFalse)
admin.site.register(OpenEnded)
admin.site.register(MultipleChoice)
admin.site.register(choice)


