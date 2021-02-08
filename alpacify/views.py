from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . forms import UploadImageForm, ShareFluffForm
from . models import Image
from . alpacify import alpacify
import hashlib

def index(request):
    return render(request, 'alpacify/index.html', None)

def upload(request):
    cxt = {'success': False, 'noface': False, 'img': ''}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['img']
            cxt['success'] = True
            alpacified, cxt['face'] = alpacify(f.read())
            cxt['img'] = 'data:{};base64,{}'.format(f.content_type,alpacified)
    return render(request, 'alpacify/alpacify.html', cxt)

def share(request):
    cxt = {'valid': False}
    if request.method == 'POST':
        form = ShareFluffForm(request.POST)
        if form.is_valid():
            img = request.POST['img']
            cxt['valid'] = True
            i = Image(image_b64 = img,
                      image_hash = hashlib.md5(img.encode('utf-8')).hexdigest())
            i.save()
    return render(request, 'alpacify/share.html', cxt)

def credits(request):
    cxt = { 'viking_web': 'http://erikbergenholtz.se',
            'viking':     'Erik Bergenholtz',
            'kenny_web':  'https://github.com/KilledKenny',
            'kenny':      'Simon Rawet',
          }
    return render(request, 'alpacify/credit.html', cxt)

def gallery(request):
    print(list(Image.objects.values_list('image_b64')))
    cxt = {
        'images': [img[0] for img in Image.objects.values_list('image_b64')]
    }
    return render(request, 'alpacify/gallery.html', cxt)

def contact(request):
    cxt = {'mail': 'contact@alpacify.me'}
    return render(request, 'alpacify/contact.html', cxt)

def privacy_cookies(request):
    return render(request, 'alpacify/privacy.html', None)

def about(request):
    cxt = {'wonderlan': 'https://mammaskallare.se/wonderlan/'}
    return render(request, 'alpacify/about.html', cxt)
