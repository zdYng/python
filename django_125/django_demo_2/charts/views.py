from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from charts.models import Chart
# from django.http import JsonResponse
def index(request):
    # template = loader.get_template('charts/index.html')
    # context = { 'balabal'}
    # return HttpResponse(template.render(context))
    # return HttpResponse('<h1>Hello</h1>')
    return render(request,'charts/index.html')

def demo_1(request):
    List = [{'list1':'123','list2':'1233'},{'list1':'12s3','list2':'123s3'}]
    return render(request,'charts/demo_1.html',{'List':List})
import json
def charts_data(request):
    lists = list(Chart.objects.values('time','predict'))
    lists = json.dumps(lists,indent=4)

    return render(request,'charts/demo_2.html',{'lists':lists})

def charts_data_2(request):
    lists = list(Chart.objects.values('time', 'predict'))
    lists = json.dumps(lists, indent=4)
    return HttpResponse(lists)


