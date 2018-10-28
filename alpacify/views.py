from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . forms import UploadImageForm
from . alpacify import alpacify

def index(request):
    return render(request, 'alpacify/index.html', None)

def upload(request):
    cxt = {'success': False, 'img': ''}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['img']
            cxt['success'] = True
            cxt['img'] = 'data:{};base64,{}'.format(f.content_type,alpacify(f.read()))
    return render(request, 'alpacify/alpacify.html', cxt)

def credits(request):
    cxt = { 'viking_web': 'http://erikbergenholtz.se',
            'viking':     'Erik Bergenholtz',
            'kenny_web':  'https://github.com/KilledKenny',
            'kenny':      'Simon Rawet',
          }
    return render(request, 'alpacify/credit.html', cxt)

def gallery(request):
    return render(request, 'alpacify/todo.html', None)

def contact(request):
    cxt = {'mail': 'contact@alpacify.me'}
    return render(request, 'alpacify/contact.html', cxt)

def privacy_cookies(request):
    return render(request, 'alpacify/privacy.html', None)

def about(request):
    cxt = {'wonderlan': 'https://mammaskallare.se/wonderlan/'}
    return render(request, 'alpacify/about.html', cxt)
