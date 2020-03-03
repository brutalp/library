from django.urls import path
from login_app.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]
