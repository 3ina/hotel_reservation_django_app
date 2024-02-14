from django.shortcuts import render

def index(request):

    return render(request,'backend/index.html',{})


def about(request):
    return render(request, 'backend/about.html', {})

def term_conditions(request):
    return render(request,'backend/term-conditions.html',{})