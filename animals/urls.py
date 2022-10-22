from django.urls import path
from animals.views import index


app_name = 'animals'
urlpatterns = [
    path('', index, name='index')
]