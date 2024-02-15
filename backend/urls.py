from django.urls import path
from backend import views

app_name = "backend"

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('term-conditions/', views.term_conditions, name='term-conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('team/', views.TeamMemberView.as_view(), name="team")
]


