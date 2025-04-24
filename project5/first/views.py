from django.shortcuts import render
from . forms import contactForm, PasswordValidationProject
def home(request):
    return render(request, './first/home.html')
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './first/about.html', {'name' : name, 'email' : email, 'select' : select})
    else:
     return render(request, './first/about.html')
def submit_form(request): 
        return render(request, './first/form.html')
def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, './first/django_form.html', {'form':form})
    else:
        form = contactForm()
    return render(request, './first/django_form.html', {'form':form})


# def StudentForm(request):
#     if request.method == 'POST':
#         form = StudentData(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = StudentData()
#     return render(request, './first/django_form.html', {'form':form}) 


def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(request, './first/django_form.html', {'form':form})