from django.urls import path

from . import views

app_name = 'verde'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_data/', views.get_data, name='get_data'),
]