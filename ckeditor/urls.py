import django

from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache
from django.conf.urls import url

from ckeditor import views

if django.VERSION >= (1, 8):
    urlpatterns = [
        url(r'^upload/', staff_member_required(views.upload), name='ckeditor_upload'),
        url(r'^browse/', never_cache(staff_member_required(views.browse)), name='ckeditor_browse'),
    ]
else:
    print("####################")
    print("aqui")
    print("####################")
    from django.conf.urls import patterns
    urlpatterns = patterns(
        '',
        url(r'^upload/', staff_member_required(views.upload), name='ckeditor_upload'),
        url(r'^browse/', never_cache(staff_member_required(views.browse)), name='ckeditor_browse'),
    )
