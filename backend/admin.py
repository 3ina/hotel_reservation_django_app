from django.contrib import admin
from backend import models

admin.site.register(models.Post)
admin.site.register(models.Tag)
admin.site.register(models.TagPost)
admin.site.register(models.RestaurantItem)
admin.site.register(models.TeamMember)
admin.site.register(models.GalleryImage)





