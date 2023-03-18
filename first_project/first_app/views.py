from django.shortcuts import render
from django.http import HttpResponse
from . models import Topic,Webpage 
# Create your views here.
def index(request):
    # my__dict={"data":"hello hi"}
    data=Topic.objects.values_list('top_name')
    my__dict={'data':data}
    print(my__dict)
    return render(request,'index.html',context=my__dict)
    # return HttpResponse("hello")