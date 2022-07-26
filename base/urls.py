
from django.urls import path
from . import views
from .views import Add_receipt, Update,Account,MyLoginView, Delete
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('', views.home, name='home' ),
    path('register', views.register, name='register' ),
    path('login', MyLoginView.as_view(template_name='login.html'),name='login' ),
    path('logout', auth_views.LogoutView.as_view(),name='logout' ),
    path('account/<str:username>/', Account.as_view(),{'next_page': '/login'}, name='account'),
    path('medicine/<int:pk>/update',Update.as_view(), name='update'),
    path('medicine/<int:pk>/delete',Delete.as_view(), name='delete'),
    path('add_receipt', Add_receipt.as_view(), name='add_receipt'),
    
]