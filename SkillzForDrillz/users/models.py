from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=75)
    profile = models.ImageField(default='faceless.png', blank=True)

    def __str__(self):
        return self.title