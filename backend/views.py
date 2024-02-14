from django.shortcuts import render

def index(request):

    return render(request,'backend/index.html',{})


def about(requst):
    return render(requst,'backend/about.html',{})