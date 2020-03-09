from django.urls import path, include
from login_app.views import LoginView, CheckView, HelloView
from . import views

urlpatterns = [
    path('', LoginView.as_view()),
    # path('check/', CheckView.as_view()),
    # path('hello/', HelloView.as_view()),
]
