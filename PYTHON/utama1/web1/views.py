from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'Ini Home Page',
        'contents' : 'Ini adalah kontennya'
    }

    return render(request,'index.html', context)