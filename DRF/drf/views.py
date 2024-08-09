from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request,'login')

def register(request):
    return render(request,'register.html')

def view(request):
    return render(request,'view.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'def')



