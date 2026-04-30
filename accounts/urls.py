from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    path('magic/', views.magic_link_view, name='magic_link'),
    path('magic/<uuid:token>/', views.magic_verify_view, name='magic_verify'),
]
