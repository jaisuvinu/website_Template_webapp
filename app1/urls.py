
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homel'),
    path('home/', home, name='homel'),
    path('about/', about, name='aboutl'),
    path('contact/', contact, name='contactl')

]

