from django.urls import path
from backend import views

app_name = "backend"

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('term-conditions/', views.term_conditions, name='term-conditions'),

]

