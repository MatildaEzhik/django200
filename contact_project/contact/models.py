from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'{self.name} - {self.email}'
