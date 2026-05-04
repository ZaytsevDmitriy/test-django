from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect,HttpResponseBadRequest, HttpResponseForbidden


# Create your views here.
def index(request):
    # return render(requst, 'firstapp\home.html')
    header = 'Персональные данные'
    langs = ['Английский', "Немецкий", 'Испанский']
    user = {'name': 'Максим', 'age': 18}
    addr = ("Виноградная", 23, 45)
    data = {"header":header, "langs": langs, "user": user, "addr": addr}
    return render(request, "index.html", data)
def about(request):
    return HttpResponse('<h2>О сайте<h2>')
def contact(requst):
    return HttpResponseRedirect('/about')
    #return HttpResponse('<h2> Контакты<h2>')
def product(request, productid=1):
    category = request.GET.get("cat", "Не задано")
    output = '<h2>Продукт № {0} Категория {1}</h2>'.format(productid, category)
    return HttpResponse(output)
def user(request):
    id = request.GET.get("id", "Не задано")
    name = request.GET.get("name", "Не задано")
    output = '<h2>Пользователь</h2><h3>id:'\
    '{0} Имя:{1}</h3>'.format(id, name)
    return HttpResponse(output)
def details(request):
    return HttpResponsePermanentRedirect('/')

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest('Некорректные данные')
    if age > 17:
        return HttpResponse('Доступ разрешен')
    else:
        return HttpResponseForbidden('Доступ запрещен')
