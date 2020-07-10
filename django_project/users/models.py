from django.db import models
from django.contrib.auth.models import User

# models.CASCADE is a one way thing, i.e. when an user is deleted, the profile is also deleted, but not the other way around.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
