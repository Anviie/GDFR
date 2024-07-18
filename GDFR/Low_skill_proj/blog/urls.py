from django.urls import path, include, re_path
from blog.views import *



urlpatterns = [
    path("index/<int:ident>/", index),
    path("access/<int:age>/", access),
]


# urlpatterns = [
#     path('', index),
#     path('about/', about),
#     path('contact/', contact),
#     path('details/', details)
# ]

# product_patterns = [
#     path('', products),
#     path('comments/', comments),
#     path('question/', question)
# ]

# urlpatterns = [
#     path('', index),
#     path('products/<int:id>/', include(product_patterns))
# ]

# urlpatterns = [
#     # path('', homepageview, name='home'),
#     # path('user/<str:name>/<int:age>/', user),
#     # path('user/<str:name>/', user),
#     path('', index, name='main'),
#     re_path(r'^contact/', contact),
#     re_path(r'^about/', about, kwargs={'name': 'Valera', 'age': '44'}),
#     re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/', user),
#     re_path(r'^user/(?P<name>\D+)/', user),
#     path('user/', user,),
    
    
# ]