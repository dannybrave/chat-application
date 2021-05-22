from django.shortcuts import render


def sign_in(request):
    context={}
    return render(request,'sign-in.html',context)