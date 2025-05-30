from django.urls import path
from . import views
from .api_views import ItemListCreateAPI, ItemDetailAPI
from .api_views import UserProfileAPI

urlpatterns = [
    path('', views.home_view, name='home'),
    path('report/', views.report_item, name='report_item'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('newsfeed/', views.newsfeed_view, name='newsfeed'),
    path('api/items/', ItemListCreateAPI.as_view(), name='api-items'),
    path('api/profile', UserProfileAPI.as_view(), name='api-profile'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
]


