from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post, Tag

def front(request):
    context = {}
    return render(request, 'front.html', context)


def post_previews(request):

    page = int(request.GET.get('page', 0))
    page_size = int(request.GET.get('page_size', 3))

    # page_size = 3

    start = page * page_size
    end = (page + 1) * page_size

    posts = Post.objects.all().order_by('-date_posted')[start:end]
    if len(posts) > 0:
        return render(request, 'post-preview.html', {'posts': posts})
    else:
        return HttpResponse('')

def get_post(request, id):
    context = {}

    if request.method == 'GET':
        post = Post.objects.get(id=id)
        context['post'] = post
        context['tags'] = post.tags.all()

        return render(request, 'post.html', context)
