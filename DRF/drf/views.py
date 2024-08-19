from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request,'home.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete')