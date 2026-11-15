from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Post


def home(request):
    posts = Post.objects.filter(
        is_published=True
    ).order_by("-published_at", "-id")

    return render(
        request,
        "blog/home.html",
        {"posts": posts}
    )


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = PostForm()

    return render(
        request,
        "blog/create_post.html",
        {"form": form}
    )