from django.shortcuts import render


def index(request):
    context={}
    return render(request,'sign-in.html',context)