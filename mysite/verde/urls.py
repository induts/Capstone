from django.urls import path

from . import views

app_name = 'verde'
urlpatterns = [
    path('index', views.index, name='index'),
    path('get_data/', views.get_data, name='get_data'),
    path('', views.home, name='Home'),
    path('about', views.about, name='about'),
]

