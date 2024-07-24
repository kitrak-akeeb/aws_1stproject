from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='cars/',default='F:/AWS_Project/sorry.jpg')
   

    def __str__(self):
        return self.name
    
    

