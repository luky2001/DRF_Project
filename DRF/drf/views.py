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
    return render()