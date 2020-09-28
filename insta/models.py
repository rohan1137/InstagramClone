from django.db import models
from django.utils import timezone

# Create your models here.

#Step - 1
class Post(models.Model):
    """
        Post model which handles the Post from the user.
    """
    author = models.ForeignKey('auth.user', on_delete= models.CASCADE)
    image = models.ImageField(blank= True, null= True)
    caption = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)
