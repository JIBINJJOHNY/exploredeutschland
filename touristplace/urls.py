from django.urls import path, include
from . import views
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('state_detail/<int:state_id>/', views.state_detail, name='state_detail'),
    

    # Create (Add a Review)
    path('add_review/<int:tourist_place_id>/', views.add_review, name='add_review'),

    # Read (View Reviews)
    path('tourist_place/<int:tourist_place_id>/reviews/', views.view_reviews, name='tourist_place_ratings'),

    # Update (Edit a Review)
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),

    # Delete (Remove a Review)
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),

    path('place/<int:place_id>/', views.place_details, name='place_details'),
    path('get_large_image/<int:image_id>/', views.get_large_image, name='get_large_image'),
    path('account/settings/', views.account_settings, name='account_settings'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('search/', views.search_view, name='search'),
    path('update-booking/<int:pk>/', views.BookingUpdateView.as_view(), name='update_booking'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]




   

    
    
