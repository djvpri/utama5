from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'Ini Blog',
        'contents' : 'Ini konten dari blog'
    }

    return render(request, 'blog/index.html', context)