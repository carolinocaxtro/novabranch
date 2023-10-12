from django.urls import path
from . import views  # Importe as views da sua aplicação

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]