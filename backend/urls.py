from django.urls import path
from backend import views

app_name = "backend"

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('term-conditions/', views.term_conditions, name='term-conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('team/', views.TeamMemberView.as_view(), name="team"),
    path("gallary/",views.hotel_room_gallery,name="gallery-hotel-room"),
    path("gallary/conference/", views.conference_gallery, name="gallery-Conference"),
    path("gallary/resort-reserve/", views.resort_reserve, name="Resort-Reserve"),
    path("gallary/weeding-hall/", views.weeding_hall, name="weeding-hall"),

]


