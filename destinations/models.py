from django.db import models
from django.utils.text import slugify

class Destinations(models.Model):
    """Destinations model"""
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Destination Name',
        help_text='Required. Max length: 100 characters'
    )
    description = models.TextField(
        null=False,
        verbose_name='Destination Description',
        help_text='Required'
    )
    location = models.CharField(
        max_length=100,
        null=False,
        verbose_name='Destination Location',
        help_text='Required. Max length: 100 characters'
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Destination Slug',
        help_text='Required. Max length: 150 characters'
    )
    
    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    @classmethod
    def get_active_destinations(cls):
        """Get active destinations"""
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_not_active_destinations(cls):
        """Get not active destinations"""
        return cls.objects.filter(is_active=False)
