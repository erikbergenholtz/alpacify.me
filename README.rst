===========
Alpacify.Me
===========

Alpacify.Me is a website built with one purpose; showing you what you'd look
like if you were a fluffy alpaca. The @KilledKenny came up with the idea during
a programming competition for a LAN party, and we implemented the original
version in Python and PHP together.

This repo contains a Django port of the original code. The functionality is the
same, but the code is a lot cleaner.

Dependencies
------------
The project requires Python3.x, and relies on a few libraries. The dependencies
that are avaiable via ``pip`` are listed in ``requirement.txt``. For the other
dependencies, please look up how to install them on your distribution. The
instructions below are for ``apt`` based systems only.

    pip install -r requirements.txt
    apt install python3-opencv

Installation
------------
When you have installed the dependencies, you need to create a new Django
project to run Alpacify in. Once you've go the Django project, you can clone
this repo::

  mkdir thesite ; cd !*
  django-admin startproject mysite
  git clone git@github.com:ErikBergenholtz/alpacify.me.git
  mv alpacify.me/alpacify mysite

Now all you need to do is add Alpacify to ``mysite/settings.py`` and
``mysite/urls.py``. They should look something like this::

  # mysite/settings.py
  INSTALLED_APPS = [
      'alpacify.apps.AlpacifyConfig',
      ...
  ]

  # mysite/urls.py
  urlpatterns = [
      path('', include('alpacify.urls')),
      ...
  ]

Once this is done, you should be able to test the application with the builtin
webserver in Django by running ``mysite/manage.py runserver`` and going to
``localhost:8000``.

Supported image formats
-----------------------
AlpacifyMe is supports alpacifying the following image formats:

* JPEG
* PNG
* BMP
