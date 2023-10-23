from django.urls import path
from . import views


urlpatterns = [
    path('', views.PackageListView.as_view(), name='package-list'),
    path('<int:pk>/', views.PackageDetailView.as_view(), name='package-detail'),
    path('bookings/', views.booking_list, name='booking_list'),

    # URL pattern for the booking detail view, using the booking_id as a parameter
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),

    # URL pattern for the booking create view
    path('bookings/create/<int:package_id>/', views.booking_create, name='booking_create'),
    path('book/<int:booking_id>/', views.book_now, name='book_now')

]
