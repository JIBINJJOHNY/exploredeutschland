from django import forms
from .models import Booking
from django.contrib.auth import get_user_model

class BookingForm(forms.ModelForm):
    user_full_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'User Full Name'}))

    class Meta:
        model = Booking
        fields = ['user_full_name', 'date', 'no_of_guests', 'package', 'payment_method', 'contact_email', 'contact_phone', 'special_requests']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BookingForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user_full_name'].initial = user.get_full_name()
            self.fields['user_full_name'].widget.attrs['readonly'] = True
        else:
            self.fields['user_full_name'].widget = forms.HiddenInput()

        # Customize the date widget for the "date" field
        self.fields['date'].widget = forms.DateInput(
            attrs={'type': 'date', 'class': 'your-custom-class'}
        )

    def clean_no_of_guests(self):
        no_of_guests = self.cleaned_data['no_of_guests']
        if no_of_guests < 1 or no_of_guests > 6:
            raise forms.ValidationError("Number of guests must be between 1 and 6.")
        return no_of_guests
