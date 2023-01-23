from django.shortcuts import render
from app1.models import *
# Create your views here.
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topic name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is inserted successfully')

def insert_Webpage(request):
    tn=input('enter topic_name')
    name=input('enter name')
    url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('webpage data is insterted')

def insert_AccessRecord(request):
    tn=input('enter a topic name')
    name=input('enter name of')
    url=input('enter url')
    date=input('enter date')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    A=AccessRecord.objects.get_or_create(name=W,date=date)[0]
    A.save()
    return HttpResponse('Accessrecords created successfully')