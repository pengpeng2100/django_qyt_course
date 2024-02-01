from django.shortcuts import render


def qytang_index(request):
    return render(request, 'index.html')
