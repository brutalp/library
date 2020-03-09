from django.urls import path, include
from login_app.views import LoginView, CheckView, HelloView
from . import views

urlpatterns = [
    path('', views.index),
    # path('check/', CheckView.as_view()),
    # path('hello/', HelloView.as_view()),
]
