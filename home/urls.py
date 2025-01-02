from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from home import views
from rest_framework.routers import DefaultRouter
from home.api.views import CarbonFootprintViewSet
from home.views import save_carbon_footprint, dashboard


router = DefaultRouter()
router.register('carbon-footprint', CarbonFootprintViewSet)

urlpatterns=[
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('api/', include(router.urls)),
    path('services/', views.save_carbon_footprint, name='services'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
