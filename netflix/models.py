from django.db import models

# Create your models here.

GENDER_OPTIONS = {
    ('male', 'male'),
    ('female', 'female'),
    ('others', 'others')
}

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=100 , choices=GENDER_OPTIONS , null=True) 
    profile_pic = models.ImageField(upload_to='pictures', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

