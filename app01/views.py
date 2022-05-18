from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    print("index 视图函数执行...")
    return HttpResponse("<h1>hello world</h1>")
