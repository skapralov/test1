import uuid as uuid
from django.db import models


class Request(models.Model):
    STATUS_CHOICES = (
        ('pending review', 'pending review'),
        ('under review', 'under review'),
        ('closed', 'closed'),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=14, choices=STATUS_CHOICES, default='pending review')
    description = models.TextField()

    def __str__(self):
        return f'{self.uuid} status: {self.status}'


class Offer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='offers')

    def __str__(self):
        return f'{self.uuid} price: {self.price}'
