from django.urls import path
from urllib.parse import quote

from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('images/detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
]

url = "http://127.0.0.1:8000/static/css/bookmarklet.css?r=1234567890123456"
encoded_url = quote(url) 

# python manage.py runserver_plus --cert-file cert.crt
