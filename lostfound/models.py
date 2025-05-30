from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]
    
    DISPOSITION_CHOICES = [
        ('Return','Return'),
        ('Donated','Donated'),
        ('Not claimed','Not claimed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES , default = 'lost')
    disposition = models.CharField(
        max_length=50,
        choices=[('Returned', 'Returned'), ('Claimed', 'Claimed'), ('Donated', 'Donated')],
        blank=True,
        null=True,  # ← Add this
        default=''  # ← Optional default
    )

    contact_info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items_owned')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items_reported')

    def __str__(self):
        return self.title

class LostFound_Item(models.Model):
    image = models.ImageField(upload_to='images/')  # Ensure this line is present
    # Other fields...

