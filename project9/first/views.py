from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7))
    # response.set_cookie('name', 'karim', max_age=10)
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name':name})

def delete_cookie(request):
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {
        'name' : 'rahim',
        'age' : '24',
        'language':'English'
    }
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    name = request.session.get('name', 'Guest')
    age = request.session.get('age')
    language = request.session.get('language')
    # print(data)
    return render(request,'get_session.html', {'name' : name, 'age' : age, 'language' : language})


def delete_session(request):
    # del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'del.html')