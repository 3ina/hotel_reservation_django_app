from django.urls import path
from backend import views

app_name = "backend"

urlpatterns = [
    path('',views.index,name='index')
]


