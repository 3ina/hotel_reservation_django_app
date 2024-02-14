from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):


    author = models.ForeignKey(get_user_model(),related_name="posts"
                               ,on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    image1 = models.ImageField(upload_to="./images/post/")
    image2 = models.ImageField(upload_to="./images/post/")
    upload_date = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=60)

class TagPost(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


class RestaurantItem(models.Model):
    categories = (
        ("Breakfast","Breakfast"),
        ("Lunch","Lunch"),
        ("Dinner","Dinner"),
        ("Drink","Drink"),
    )
    title = models.CharField(max_length=30)
    desc = models.TextField()
    category = models.CharField(max_length=20,choices=categories)
    image = models.ImageField(upload_to='./images/food/')
    price = models.PositiveSmallIntegerField()