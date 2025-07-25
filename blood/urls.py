
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # ✅ This handles the root URL
    path('donor/', views.show_donor_form, name='donor'),
    path('donor/submit/', views.donor_submit, name='donor_submit'),
    path('request/', views.request_form, name='getter'),
     path('request/submit/', views.match_blood_group, name='match_blood_group'),
    path('awareness/', views.awareness_page, name='aware'),
    path('register/', views.register_form, name='register'),
     path('map/', views.map_view, name='map'),
    path('chatbot/ask/', views.chatbot_response, name='chatbot_response'),
    path('chatbot/', views.chatbot_page, name='chatbot_page'),  # if using chatbot.html


]





