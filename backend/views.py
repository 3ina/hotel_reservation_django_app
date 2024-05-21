from django.contrib import messages
from django.shortcuts import render
from backend import models
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

def index(request):
    recent_posts = models.Post.objects.order_by("upload_date").all()[0:2]

    context = {

        "recent_posts": recent_posts,
    }
    return render(request, 'backend/index.html', context)


def about(request):
    return render(request, 'backend/about.html', {})


def term_conditions(request):
    return render(request, 'backend/term-conditions.html', {})


def privacy_policy(request):
    return render(request, 'backend/privacy-policy.html', {})


def restaurant(requests):
    breakfast = models.RestaurantItem.objects.filter(category='Breakfast')
    lunch = models.RestaurantItem.objects.filter(category='Lunch')
    dinner = models.RestaurantItem.objects.filter(category='Dinner')
    drink = models.RestaurantItem.objects.filter(category='Drink')

    context = {
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,
        "drink": drink,

    }
    return render(requests, 'backend/restaurant.html', context)


class TeamMemberView(ListView):
    model = models.TeamMember
    paginate_by = 3
    template_name = 'backend/team.html'


def hotel_room_gallery(request):
    objects = models.GalleryImage.objects.filter(category="Hotel Room")
    context = {
        "objects": objects,
    }
    return render(request, 'backend/gallery.html', context)


def conference_gallery(request):
    objects = models.GalleryImage.objects.filter(category="Conference")
    context = {
        "objects": objects,
    }
    return render(request, 'backend/gallery.html', context)


def resort_reserve(request):
    objects = models.GalleryImage.objects.filter(category="Resort Reserve")
    context = {
        "objects": objects,
    }
    return render(request, 'backend/gallery.html', context)


def weeding_hall(request):
    objects = models.GalleryImage.objects.filter(category="Weeding Hall")
    context = {
        "objects": objects,
    }
    return render(request, 'backend/gallery.html', context)


class ListBlogPost(ListView):
    model = models.Post
    paginate_by = 3
    template_name = "backend/blog.html"


def detail_blog_post(request, pk):
    post = get_object_or_404(models.Post, id=pk)
    tags = models.TagPost.objects.filter(post=post)
    comments = models.Comment.objects.filter(post=post)
    recent_posts = models.Post.objects.order_by("upload_date").all()[0:3]

    context = {
        "post": post,
        "tags": tags,
        "comments": comments,
        "recent_posts": recent_posts,
    }
    return render(request, "backend/blog-detail.html", context)


@login_required
@require_POST
def create_comment(request,pk):
    post = get_object_or_404(models.Post, id=pk)
    user = request.user
    comment_is_exists = models.Comment.objects.filter(post=post,author=user)
    if comment_is_exists.exists():
        messages.error(request, "you can write only one comment")
        return redirect("backend:post-detail", pk=pk)

    text = request.POST['message']
    comment = models.Comment.objects.create(post=post,author=user,text=text)
    comment.save()
    messages.success(request, "success")

    return redirect("backend:post-detail",pk=pk)
