from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict={'view_data':"this data is from views"}
    return render(request, 'first_app/index.html',context=my_dict)
    # return HttpResponse("<h1>hello guyzzzz...!</h1> ")
def helping(request):
    return render(request, 'second_app/second.html')