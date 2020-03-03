from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class LoginView(View):

    def get(self, request):
        return render(request, 'login_app/index.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)
