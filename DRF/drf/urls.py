
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/login/',views.login,name='login'),
    path('/logout/',views.logout,name='logout'),
    path('/profile/',views.profile,name='profile'),
    path('/update/',views.update,name='update'),
    #path('/delete/',views.delete,name='delete'),
    #path('update_profile',views.update_profile,name='up_pro'),
    #path('delete_up',views.delete_up,name,name='delete_up'),
    #path('/show/',views.show,name='show'),
    #path('/contact/',views.contact,name='contact'),
]
