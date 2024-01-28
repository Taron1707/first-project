from django.shortcuts import render


def indexs(request):
    return render(request, 'main/index.html', {'title': 'text'})


def about(request):
    return render(request, 'main/about.html')
