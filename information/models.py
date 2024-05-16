from django.db import models

# Create your models here.

class Users(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    birthplace = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    education = models.CharField(max_length=50)
    gender = models.CharField(max_length=7)
    image = models.ImageField()
    
    def __str__(self):  #convert full_name from Users class into string
        return f'{self.full_name}'
    class Meta:  
        db_table = 'user'
        
    
    