from django.db import models
from django.contrib.auth.models import User


def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    image = models.URLField(
        max_length=2000, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTayBxqNcpOECgVloLid0g8WYj7qn6w7k-dhQ&usqp=CAU")
    bio = models.TextField(max_length = 500 , blank=True)

    def __str__(self):
        return "{} {}".format(self.user, 'Profile')
