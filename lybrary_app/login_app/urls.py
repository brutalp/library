from django.urls import path, include
from login_app.views import LoginView
from . import views

urlpatterns = [
    path('', LoginView.as_view()),
    path('check/', views.check, name='check'),
    path('hello/', views.hello, name='hello'),
]
