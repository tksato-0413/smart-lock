from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('control-motor/', views.control_motor, name='control_motor'),
]
