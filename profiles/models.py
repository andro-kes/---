from django.db import models

class Profiles(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    manager = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
