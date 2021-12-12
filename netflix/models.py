from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

