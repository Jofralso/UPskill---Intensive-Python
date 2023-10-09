from django.db import models

class Contact(models.Model):
    phone= models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.phone
#One-to-One Relationship

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #relationship
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'