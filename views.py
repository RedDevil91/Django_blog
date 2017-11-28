from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostFrom
from .models import BlogPost


def view_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post.html', {'blogpost': post})


def new_post(request):
    if request.method == 'POST':
        form = PostFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(r'temp_page')
    else:
        form = PostFrom()
    return render(request, 'blog/edit.html', {'form': form})


def temp_page(request):
    return render(request, 'blog/temp_page.html')


def like_post(request):
    response = {}
    if request.method == 'POST':
        pk = request.POST.get("pk")
        post = get_object_or_404(BlogPost, pk=pk)
        post.is_starred = not post.is_starred
        post.save()
        response["state"] = "Dislike" if post.is_starred else "Like"
    else:
        response["error"] = "don't know why"
    return JsonResponse(response)


def del_post(request):
    response = {}
    if request.method == 'POST':
        pk = request.POST.get("pk")
        post = get_object_or_404(BlogPost, pk=pk)
        post.delete()
        response["state"] = True
    else:
        response["state"] = False
        response["error"] = "..."
    return JsonResponse(response)
