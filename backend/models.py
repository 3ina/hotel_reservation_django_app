from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), related_name="posts"
                               , on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    image1 = models.ImageField(upload_to="./images/post/")
    image2 = models.ImageField(upload_to="./images/post/")
    upload_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('backend:post-detail', args=[self.id])


class Tag(models.Model):
    name = models.CharField(max_length=60)


class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name="comments"
                               , on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
class RestaurantItem(models.Model):
    categories = (
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Drink", "Drink"),
    )
    title = models.CharField(max_length=30)
    desc = models.TextField()
    category = models.CharField(max_length=20, choices=categories)
    image = models.ImageField(upload_to='./images/food/')
    price = models.PositiveSmallIntegerField()


class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='./image/team/')
    position = models.CharField(max_length=30)
    instagram = models.CharField(max_length=60,null=True,default=None)
    twitter = models.CharField(max_length=60,null=True,default=None)
    facebook = models.CharField(max_length=60,null=True,default=None)
    pinterest = models.CharField(max_length=60,null=True,default=None)



class GalleryImage(models.Model):
    categories = (
        ("Hotel Room", "Hotel Room"),
        ("Conference", "Conference"),
        ("Resort Reserve", "Resort Reserve"),
        ("Weeding Hall", "Weeding Hall"),
    )
    image = models.ImageField(upload_to='./image/gallery/')
    category = models.CharField(max_length=20,choices=categories)