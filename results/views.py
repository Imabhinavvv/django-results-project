from django.shortcuts import render
from .models import Results

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if  request.method =="POST":
        roll_number = request.POST.get('roll_number')
        result= Results.objects.get(roll_number=roll_number)
        context={'result': result}
        return render(request, 'results.html',context)