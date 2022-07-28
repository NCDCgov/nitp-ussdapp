# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('customer/', admin.site.urls),
# ]

# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]