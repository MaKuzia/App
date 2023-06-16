from django.urls import path

from bid import views

app_name = 'bid'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('bids/<int:bid_id>/', views.bid_detail, name='bid_detail'),
    path('create/', views.bid_create, name='bid_create'),
    path('bids/<int:bid_id>/edit/', views.bid_edit, name='bid_edit')
]