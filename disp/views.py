from django.shortcuts import render, redirect

# Create your views here.
# encoing: utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from .models import *

def index(request):
    template= get_template('index.html')
    nowtime= datetime.now()
    userlists = list()
    userlists.append({'name':'kkk'})
    userlists.append({'name':'lll'})
    # userlists.append({'name':'Rdasdas'})
    html = template.render(locals())
    return HttpResponse(html)
def about(request):
    return HttpResponse("--------------------------\n"
                        "五个来自华侨计算机学院的2016届学生\n"
                        "--------------------------")
def hello(request,name):
    return HttpResponse("Hello "+name)

def showFacility(request):
    template = get_template('Facility.html')
    f_list = Facility.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

def facilityDetail(request,fid):
    t = get_template('facilityDetail.html')
    try:
        f=Facility.objects.get(fid=fid)
        if f != None:
            html = t.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')


