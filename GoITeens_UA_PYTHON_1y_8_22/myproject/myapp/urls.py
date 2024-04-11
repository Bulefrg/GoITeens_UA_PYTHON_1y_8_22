from django.urls import path
from . import views
from .views import reserve_table

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('dishes/', views.dishes_demo, name='dishes'),
    path('reviews/', views.reviews, name='reviews'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('reserve_table/', reserve_table, name='reserve_table'),

]
