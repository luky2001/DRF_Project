from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'base.html')
def update(request):
    return render(request,'update.html')
def delete(request):
    return render(request,'delete')
def profile(request):
    return render(request,'profile')
def customer(request):
    return render(request,'customer.html')
def product(request):
    return render(request,'product')
def show(request):
    return render(request,'show.html')
def login(request):
    return render(request,'lohin.html')
def logout(request):
    return render(request,'logout')
def list(request):
    return render(request,'list')
def register(request):
    return render(request,'')