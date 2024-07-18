from django.shortcuts import render
# HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden




def index(request, ident):
    people = [None, 'Bob', 'Sam', 'Tom']
    if ident in range(1, len(people)):
        return HttpResponse(people[ident])
    else:
        return HttpResponseNotFound('Пользователь не найден')
    
def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest('Не корректные данные')
    if (age>17):
        return HttpResponse('Доступ разрещён')
    else:
        return HttpResponseForbidden('Доступ заблокирован - слишком юн')
    





# def index(request):
#     return HttpResponse('Нету', status=404)

# def index(request):
#     return HttpResponseNotFound('Нет такой страницы')

# def index(request):
#     return HttpResponse('main')

# def about(request):
#     return HttpResponse('About')

# def contact(request):
#     return HttpResponseRedirect('/about')

# def details(request):
#     return HttpResponsePermanentRedirect('/')

# def index(request):
#     return HttpResponse('Главаня страница')

# def user(request):
#     age = request.GET.get('age', 0)
#     name = request.GET.get('name', 'Undefined')
#     return HttpResponse(f'<h2>Имя: {name}, Возвраст: {age}</h2>')

# def products(request, id):
#     return HttpResponse('Товар')

# def comments(request, id):
#     return HttpResponse('Комментарии о товаре')

# def question(request, id):
#     return HttpResponse('Вопросы о товаре')


# def homepageview(request):
#     return HttpResponse('Hello, world!')

# def index (request):
#     return HttpResponse('''<h2>Главная</h2><br>
#                         <a href="http://127.0.0.1:8000/about">О пользователе</a><br>
#                         <a href="http://127.0.0.1:8000/contact">Контакты</a><br>
#                         <a href="http://127.0.0.1:8000/user">Пользователь</a><br>''')

# def about(request, name, age):
#     return HttpResponse(f'''<h2>О пользователе</h2>
#                         <p>Имя: {name}</p>
#                         <p>Возвраст: {age}</p>
#                         ''')

# def contact(request):
#     return HttpResponse('<h2>Контакты</h2>')

# def user(request, name='Undefined', age=0):
#     return HttpResponse(f'<h2>Пользователь:</h2><br><h5>{name} : {age}</h5>')