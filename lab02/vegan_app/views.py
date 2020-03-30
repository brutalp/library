from django.shortcuts import render
from django.views.generic import View
from .settings.base import *


class IndexView(View):

    def get(self, request):
        return render(request, 'vegan_app/index.html', {'phone_number': PHONE_NUMBER})
