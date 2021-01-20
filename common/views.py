from django.shortcuts import render


def index(request):
    return render(request, 'dust_checker/dust_main.html')