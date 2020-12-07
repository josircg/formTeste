"""formuv1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

#from .login import LoginRevista
from . import views
from .revista import Revistas
from .revista import Login

login=Login()
revistas=Revistas()

urlpatterns = [

    #path('admin/', admin.site.urls),
    path('login/', login.user_login, name='login'),
    path('revista/', revistas.revista, name='revista'),
    path('order/', revistas.revista, name='order'),
    path('form/', views.form_teste, name='form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
