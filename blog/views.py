from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Poster
from .forms import PosterForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    page = request.GET.get('page', '1')
    poster_list = Poster.objects.order_by('-create_date')
    paginator = Paginator(poster_list, 10)
    page_obj = paginator.get_page(page)
    context = {'poster_list': page_obj}
    return render(request, 'index.html', context)


def post(request):
    poster_list = Poster.objects.order_by('-create_date')
    context = {'poster_list': poster_list}
    return render(request, 'blog/post.html', context)


def detail(request, poster_id):
    poster = get_object_or_404(Poster, pk=poster_id)
    context = {'poster': poster}
    return render(request, 'blog/poster_detail.html', context)


@login_required(login_url='common:login')
def poster_create(request):
    if request.method == "POST":
        form = PosterForm(request.POST)
        if form.is_valid():
            poster = form.save(commit=False)
            poster.author = request.user
            poster.create_date = timezone.now()
            poster.save()
            return redirect('blog:post')
    else:
        form = PosterForm()
    context = {'form': form}
    return render(request, 'blog/poster_form.html', context)
