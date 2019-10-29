from django.urls import path
from django.contrib.auth import views as auth_views
from .mushroom_form import form


# from . import views

urlpatterns = [
    path('', form, name='form'),
    path('form/', form, name='form'),
]