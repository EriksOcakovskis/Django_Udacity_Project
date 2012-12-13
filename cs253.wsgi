import os
import sys
sys.path = ['/home/ocakovskise/Dropbox/coding/web/Django_Udacity_Project/cs253/cs253'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'cs253.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
