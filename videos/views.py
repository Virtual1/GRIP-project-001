from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import videos

def index(request):
    videos = videos.objects.order_by('-publish_date')

    paginator = Paginator(videos, 9)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)

    context = {
        'videos': paged_videos
    }

    return render(request, 'videos/inthemix.html', context)

def video(request, video_id):
    video = get_object_or_404(videos, pk=video_id)

    context = {
        'video': video
    }

    return render(request, 'videos/video.html', context)


def search(request):

    context = {
        'techstack': techstack
    }
    return render(request, 'videos/search.html', context)