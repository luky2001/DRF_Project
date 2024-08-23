from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request,'home.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete')

def profile(request):
    return render(request,'profile.html')

def page(request):
    return render(request,'page.html')

def customer(request):
    return render(request,'customer.html')
def update(request):
    return render(request,)
def show(request):
    return render