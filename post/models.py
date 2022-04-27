from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(
        max_length=200,
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
