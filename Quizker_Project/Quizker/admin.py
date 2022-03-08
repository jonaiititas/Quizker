from django.contrib import admin
from Quizker.models import Category,Quiz,TrueOrFalse,OpenEnded,MultipleChoice,Choice
class QuizAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('title',)}
admin.site.register(Category)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(TrueOrFalse)
admin.site.register(OpenEnded)
admin.site.register(MultipleChoice)
admin.site.register(Choice)


