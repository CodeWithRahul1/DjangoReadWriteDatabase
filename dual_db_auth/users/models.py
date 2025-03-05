from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    def save(self, *args, **kwargs):
        """Ensure data is saved in both databases."""
        super().save(using='write_db', *args, **kwargs)
        super().save(using='read_db', *args, **kwargs)

class Product(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('purchased', 'Purchased'),
        ('sold', 'Sold'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    product_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
