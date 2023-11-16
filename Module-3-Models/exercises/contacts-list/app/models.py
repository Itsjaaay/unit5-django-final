
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

from .models import Contact

def create_contact(name, email, phone, is_favorite=False):
    contact = Contact.objects.create(name=name, email=email, phone=phone, is_favorite=is_favorite)
    return contact

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(name):
    return Contact.objects.filter(name__icontains=name)

def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, new_email):
    contact = Contact.objects.get(name=name)
    contact.email = new_email
    contact.save()
    return contact

def delete_contact(name):
    contact = Contact.objects.get(name=name)
    contact.delete()