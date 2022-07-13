from django.shortcuts import render, get_object_or_404
from .models import Poster


def index(request):
    poster_list = Poster.objects.order_by('-create_date')
    context = {'poster_list': poster_list}
    return render(request, 'index.html', context)


def post(request):
    poster_list = Poster.objects.order_by('-create_date')
    context = {'poster_list': poster_list}
    return render(request, 'blog/post.html', context)


def detail(request, poster_id):
    poster = get_object_or_404(Poster, pk=poster_id)
    context = {'poster': poster}
    return render(request, 'blog/poster_detail.html', context)