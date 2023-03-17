from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my__dict={"data":"hello hi"}
    return render(request,'index.html',context=my__dict)
    # return HttpResponse("hello")