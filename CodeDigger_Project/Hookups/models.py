from django.db import models

# Create your models here.
class Join(models.Model):
    name=models.CharField(max_length=120)
    title=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
        return self.title
    