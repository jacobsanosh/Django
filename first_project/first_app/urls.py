from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('help',views.helping,name='helping')
]