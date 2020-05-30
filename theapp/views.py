from django.shortcuts import render

# Create your views here.

def main(requests):
    return render(requests, 'main.html')

def photos(requests):
    return render(requests, 'photos.html')

def intro(requests):
    return render(requests, 'intro.html')

def ex20200602(requests):
    return render(requests, 'ex20200602.html')
