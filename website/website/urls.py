from django.contrib import admin
from django.urls import path
from signup.views import signup
from login.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('login/', login),   
]
