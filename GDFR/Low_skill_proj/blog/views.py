from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def homepageview(request):
#     return HttpResponse('Hello, world!')

def index (request):
    return HttpResponse('''<h2>Главная</h2><br>
                        <a href="http://127.0.0.1:8000/about">О пользователе</a><br>
                        <a href="http://127.0.0.1:8000/contact">Контакты</a><br>
                        <a href="http://127.0.0.1:8000/user">Пользователь</a><br>''')

def about(request, name, age):
    return HttpResponse(f'''<h2>О пользователе</h2>
                        <p>Имя: {name}</p>
                        <p>Возвраст: {age}</p>
                        ''')

def contact(request):
    return HttpResponse('<h2>Контакты</h2>')

def user(request, name='Undefined', age=0):
    return HttpResponse(f'<h2>Пользователь:</h2><br><h5>{name} : {age}</h5>')