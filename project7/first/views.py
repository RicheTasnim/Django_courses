from django.shortcuts import render
from first.forms import StudentForm
# from . models import Teacher, Student
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form' : form})