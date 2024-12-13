from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('hobbies/add/', views.add_hobby, name='add_hobby'),
    path('hobbies/<int:hobby_id>/', views.hobby_detail, name='hobby_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/add/', views.add_portfolio_item, name='add_portfolio_item'),
    path('portfolio/<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
