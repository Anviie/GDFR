from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', homepageview, name='home'),
    path('user/<slug:name>/<int:age>/', user,),
    path('user/<slug:name>/', user,),
    path('user/', user,),
    re_path(r'^about/', about, kwargs={'name': 'Valera', 'age': '44'}),
    re_path(r'^contact/', contact),
    path('', index, name='main'),
]