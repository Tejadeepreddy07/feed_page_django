from django.db import models

# Create your models here.
class feed(models.Model):
    person=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    tile=models.CharField(max_length=100)
    image=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=50)

    def __str__(self):
        return self.person
