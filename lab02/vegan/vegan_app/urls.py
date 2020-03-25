from django.urls import path
from . import views
from vegan_app.views import *

urlpatterns = [
    path('', IndexView.as_view()),
]
