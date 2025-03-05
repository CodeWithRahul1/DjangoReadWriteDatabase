from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from django.db import connections
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connections
from .models import Product


User = get_user_model()

@receiver(post_save, sender=User)
def copy_user_to_read_db(sender, instance, created, **kwargs):
    if created:  # Only copy when a new user is created
        instance.save(using='read_db')  # Save the user in read_db

@receiver(post_save, sender=Product)
def replicate_product_to_read_db(sender, instance, **kwargs):
    if kwargs.get('raw', False):
        return  # Prevent recursion during bulk operations

    # Save product data to read_db to keep it updated
    with connections['read_db'].cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users_product (name, price, quantity, product_status, created_at) 
            VALUES (%s, %s, %s, %s, %s) 
            ON CONFLICT (id) 
            DO UPDATE SET 
                name=EXCLUDED.name, 
                price=EXCLUDED.price, 
                quantity=EXCLUDED.quantity, 
                product_status=EXCLUDED.product_status, 
                created_at=EXCLUDED.created_at
            """,
            [instance.name, instance.price, instance.quantity, instance.product_status, instance.created_at]
        )