from django.db import models



class UserText(models.Model):

    text = models.TextField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='texts', on_delete=models.CASCADE)
