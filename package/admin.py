from django.contrib import admin
from .models import Pack,Booking

@admin.register(Pack)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('state', 'package_type', 'price', 'places_limit')
    list_filter = ('state', 'package_type')
    search_fields = ('state__name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'no_of_guests', 'package', 'status', 'payment_amount']
    list_filter = ['user', 'status']
    search_fields = ['user__username', 'package__state__name']