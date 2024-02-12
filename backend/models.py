from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    tags = (
        ('Hotel', 'Hotel'),
        ('Single', 'Single'),
        ('Family', 'Family'),
        ('sea View', 'sea View'),

    )

    author = models.ForeignKey(get_user_model(),related_name="posts"
                               ,on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    image1 = models.ImageField(upload_to="/images")
    image2 = models.ImageField(upload_to="/images")

class Tag(models.Model):
    name = models.CharField(max_length=60)

class TagPost(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE,primary_key=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,primary_key=True)