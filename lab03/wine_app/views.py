from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from wine_app.models import Wines, People
from django.core.paginator import Paginator
from django.urls import reverse
import json


class IndexView(View):

    def get(self, request):
        wines = [
            {'title': 'Trius Cabernet France 2011',
             'price': '$629.00',
             'img': '/static/wine_app/images/wine_2.png'},
            {'title': 'Trius Cabernet France 2012',
             'price': '$629.00',
             'sale_price': '$900.00',
             'img': '/static/wine_app/images/wine_3.png'},
            {'title': 'Trius Cabernet France 2013',
             'price': '$629.00',
             'img': '/static/wine_app/images/wine_1.png'},
        ]
        people = People.objects.all()
        return render(request, 'wine_app/index.html', {'wines': wines, 'people': people})


class AboutView(View):

    def get(self, request):
        return render(request, 'wine_app/about.html')


wine_count = 0


class ShopView(View):

    def get(self, request, page_id=1):
        wines_list = Wines.objects.all()
        if not request.is_ajax():
            paginator = Paginator(wines_list, 3)
            try:
                wines = paginator.page(page_id)
                wines.num_pages_tuple = tuple(range(paginator.num_pages))
            except:
                return redirect(reverse('shop'))
            return render(request, 'wine_app/shop.html', {'wines': wines})
        else:
            print('###############################################################')
            print(json.dumps({'wines': wines_list}))
            print('###############################################################')
            return HttpResponse(json.dumps({'wines': wines_list}), content_type='application/json')

    # def post(self, request):
    #     global wine_count
    #     if request.is_ajax():
    #         message = f'ShopListView: {wine_count}'
    #         wine_count += 1
    #         print(message)
    #     else:
    #         message = 'not AJAX request'
    #
    #     return HttpResponse(message)


class ContactView(View):

    def get(self, request):
        return render(request, 'wine_app/contact.html')
