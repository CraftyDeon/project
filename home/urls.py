from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('form/',views.form,name='form'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]