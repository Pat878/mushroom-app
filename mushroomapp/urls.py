from django.urls import path
from django.contrib.auth import views as auth_views
from . import form

from . import views

urlpatterns = [
    path('', form.form, name='form'),
    path('form/', form.form, name='form'),
]