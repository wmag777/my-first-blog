from django.shortcuts import render
from django.utils import timezone
from .models import Post
from pprint import pprint
from inspect import getmembers

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    var = repr(posts)
    return render(request, 'blog/post_list.html', {'posts': posts, 'vars': var})