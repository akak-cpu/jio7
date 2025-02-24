from django.db import models

# Create your models here.
class Musiclist(models.Model):
    id=models.AutoField
    song_name=models.CharField(max_length=100,default="")
    song_catagary=models.CharField(max_length=100,default="")
    song_date=models.DateField(default="")
    song_details=models.CharField(max_length=500,default="")
    song=models.FileField(default="")
    song_coverimage=models.ImageField(default="")

    def __str__(self):
        return self.song_name

# class Contact(models.Model):
#     id=models.AutoField(primary_key=True)
    