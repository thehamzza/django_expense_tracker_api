# django_expense_tracker/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL route
    path('admin/', admin.site.urls),
    path('api/', include('transactions.urls')),
]
