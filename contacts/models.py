from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
