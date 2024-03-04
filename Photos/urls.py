from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('add/', views.add, name="add"),
    path('view/<str:pk>/', views.viewimage, name='image'),
    path('delete/<str:pk>/', views.deleteimage, name='delete_image'),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name='register'),
    path('about/',views.aboutsite, name='about_website')
]