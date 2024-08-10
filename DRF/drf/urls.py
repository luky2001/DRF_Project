
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/login/',views.login,name='login'),
    path('/logout/',views.logout,name='logout'),
    path('/profile/',views.profile,name='profile'),
    path('/update/',views.update,name='update'),
]
