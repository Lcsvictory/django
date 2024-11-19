from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


models = [Question, Answer]
admin.site.register(models, QuestionAdmin)
# Register your models here.
