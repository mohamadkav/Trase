__author__ = 'Farzin'

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from App.models import Book, Author



@csrf_exempt
def search(request):

    if request.method == 'POST':
        print(request.body)
        Author.objects.create(first_name = 'farzin', last_name = 'hooshmand', email = request.body)
    return render(request, '../../Django/templates/form.html')


def show_search(request):
    if request.POST:
        print("POST")
        Author.objects.create(first_name = 'farzin', last_name = 'hooshmand', email = request.body)
        return render(request, '../../Django/templates/search_result.html',
            {'books': request.body, 'query': 'Created'})
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']

        books = Book.objects.filter(title__icontains=q)

        return render(request, '../../Django/templates/search_result.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')