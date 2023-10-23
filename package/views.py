from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Pack, State
from .models import Booking
from .forms import BookingForm  
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.urls import reverse
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
import smtplib
import ssl

class PackageListView(ListView):
    model = State
    template_name = 'pack_list.html'
    context_object_name = 'states'


class PackageDetailView(DetailView):
    model = State
    template_name = 'pack_detail.html'
    context_object_name = 'state'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_id = self.kwargs['pk'] 
        context['packages'] = Pack.objects.filter(state_id=state_id)
        return context

@login_required
def booking_list(request):
    # View to display a list of bookings
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})
@login_required
def booking_detail(request, booking_id):
    # View to display the details of a single booking
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

@login_required
def booking_create(request, package_id):
    # Use the 'package_id' to retrieve the selected package
    package = get_object_or_404(Pack, pk=package_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Handle the form submission
            new_booking = form.save(commit=False)  # Create the booking instance but don't save it yet
            new_booking.user = request.user  # Set the user to the currently logged-in user
            new_booking.save()  # Save the booking to the database
            return redirect(reverse('booking_detail', args=[new_booking.id]))
    else:
        # Prepopulate the form with the user's full name and the selected package
        initial_data = {
            'user_full_name': request.user.get_full_name(),
            'package': package,
        }
        form = BookingForm(initial=initial_data)

    return render(request, 'booking_form.html', {'form': form})


@csrf_protect
def book_now(request, booking_id):
    # Assuming you are passing the booking ID as an argument in the URL
    booking = Booking.objects.get(id=booking_id)
    alert_message = ""
    
    if request.method == 'POST':
        # Get the user's email from the booking object
        user_email = booking.contact_email
        
        # Create an SSL context using the system's CA certificates
        context = ssl.create_default_context()

        # Your SMTP server settings should be configured in settings.py
        smtp_server = settings.EMAIL_HOST
        smtp_port = settings.EMAIL_PORT
        from_email = settings.EMAIL_HOST_USER
        email_password = settings.EMAIL_HOST_PASSWORD  # You may want to use a safer method to store the password

        # Compose the email message
        subject = "Booking Confirmation"
        recipient_list = [user_email]

        # Get the user's full name by calling the get_full_name method
        user_full_name = booking.user.get_full_name()

        # Compose the email message including booking details
        message = f"Thank you for choosing the 'Cash' payment option. We value your booking!\n\nBooking Details:\n"
        message += f"User: {user_full_name}\n"
        message += f"Booking Date: {booking.date}\n"
        message += f"Number of Guests: {booking.no_of_guests}\n"
        message += f"Package: {booking.package}\n"
        message += f"Email: {booking.contact_email}\n"
        message += f"Contact Phone: {booking.contact_phone}\n"
        message += f"Special Requests: {booking.special_requests}\n"
        message += f"Payment Amount: €{booking.payment_amount}\n"
        message += "\nTo confirm your reservation, please contact us at your earliest convenience."
        message += "Our team is here to assist you and ensure your booking is smooth and enjoyable."
        message += "You can reach us via email at support@exploredeutschland.com or by phone at +49 1523 456 7890."
        message += "We look forward to helping you with your booking details and any special requests you may have."

        try:
            print("Before sending the email")
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            print("After sending the email")
            alert_message = "Booking successful. Check your email for confirmation."
        except Exception as e:
            print(f"Email sending failed: {str(e)}")
            return HttpResponse("An error occurred while booking.")
    
    return render(request, 'booking_detail.html', {'booking': booking, 'alert_message': alert_message})
