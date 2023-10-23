from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField 
from django.contrib.auth.models import User 


class State(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='State Name',
        help_text='Required. Max length: 100 characters'
    )
    description = models.TextField(
        verbose_name='State Description',
        help_text='Required'
    )
    image = CloudinaryField(
        'state_image',
        folder='state_images/',
        null=True,
        blank=True,
    )
    alt = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='Alt text',
        help_text='Optional. Max length: 300 characters'
    )


    def __str__(self):
        return self.name

class TouristPlace(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Destination Name',
        help_text='Required. Max length: 100 characters'
    )
    description = models.TextField(
        verbose_name='Destination Description',
        help_text='Required'
    )
    location = models.CharField(
        max_length=100,
        verbose_name='Destination Location',
        help_text='Required. Max length: 100 characters'
    )
    state = models.ForeignKey(
        State,  # Establish a ForeignKey relationship with the State model
        on_delete=models.CASCADE,  # Define the behavior on State deletion
        verbose_name='State',
        help_text='Required. Max length: 100 characters'
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='Tourist Place Slug',
        help_text='Required. Max length: 150 characters'
    )
    google_map_src = models.CharField(
        max_length=500, 
        blank=True, 
        null=True
    )
    

    class Meta:
        verbose_name = 'Tourist Place'
        verbose_name_plural = 'Tourist Places'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class TouristPlaceImage(models.Model):
    """TouristPlace image model"""
    touristplace = models.ForeignKey(
        'TouristPlace',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='TouristPlace',
        help_text='Choose the TouristPlace for this image'
    )
    image = CloudinaryField(
        'touristplace_image',
        folder='touristplace_images',
        null=True,
        blank=True,
    )
    alt_text = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='Alt text',
        help_text='Optional. Max length: 300 characters'
    )
    default_image = models.BooleanField(
        default=False,
        verbose_name='Default Image'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated at'
    )
    
    class Meta:
        verbose_name = 'Touristplace image'
        verbose_name_plural = 'Touristplace images'
        ordering = ['touristplace']
    
    def __str__(self):
        return f"Image for {self.touristplace.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.default_image:
            for image in self.touristplace.images.all().exclude(id=self.id):
                image.default_image = False
                image.save()

    
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return 'static/images/default_touristplace_image.jpeg'



class Rev(models.Model):
    """Review model."""
    STAR_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='revs',
    )
    tourist_place = models.ForeignKey(
        TouristPlace,
        on_delete=models.CASCADE,
        related_name='revs',
    )
    rating = models.IntegerField(
        choices=STAR_CHOICES,
        default=1,  # Set a default value
    )
    comment = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of model."""
        return f'{self.user.username} - {self.tourist_place.name} - {self.rating}'

    class Meta:
        """Meta class."""
        ordering = ['-created_at']
