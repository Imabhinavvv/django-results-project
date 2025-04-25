from django.contrib import admin
from .models import Branch, Results
# Register your models here.

class ResultsAdmin(admin.ModelAdmin):
    list_display= ['roll_number','name','percentage','final_result']

admin.site.register(Results,ResultsAdmin)
admin.site.register(Branch)
