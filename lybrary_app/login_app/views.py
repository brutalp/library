from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class LoginView(View):

    def get(self, request):
        return render(request, 'login_app/login.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class CheckView(View):

    def get(self, request):
        return render(request, 'login_app/check.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class HelloView(View):

    def get(self, request):
        return render(request, 'login_app/hello.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)

#
# def check(request):
#     return render(request, 'login_app/check.html')
#
#
# def hello(request):
#     return render(request, 'login_app/hello.html')
