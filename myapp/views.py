from django.shortcuts import render

# Create your views here.
def filter_demo(request):
    return render(request,"filter_demo.html",{'data':"hello world",'a':11,'b':22,'num':999})