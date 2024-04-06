"""
URL configuration for EZexchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path
from EZapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('<id>/<str:category>/', views.home, name="home"),
    path('<int:pid>/', views.product_details, name="product_details"),
    path('login/', views.UserLogin, name="UserLogin"),
    path('logout/', views.UserLogout, name="UserLogout"),
    path('register/', views.UserRegister, name="UserRegister"),
    path('account/<id>/<str:selected>/', views.Account, name="Account"),
    path('sell_item/<id>/<str:category>/', views.Category, name="Category"),  # Specific pattern
    path('sell_item/', views.sellItem, name="sellItem"),  # General pattern
    path('<pid>/send_email/<buyuser>/<selluser>/',views.send_email,name="send_email"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)