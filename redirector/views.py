from django.http import Http404
from django.conf import settings
from django.shortcuts import render_to_response, redirect
from models import Redirection, MissDirection
from django.core.exceptions import ObjectDoesNotExist

def get_missdirection(source_name):
    "Make sure we log this miss in direction"
    miss = None
    try:
        miss = MissDirection.objects.get(source_name=source_name)
        miss.count += 1
        miss.save()
    except ObjectDoesNotExist:
        miss = MissDirection(source_name=source_name, count=1)
        miss.save()

    return miss

def get_redirection(source_name):
    "Get the desired redirection"
    try:
        redirection = Redirection.objects.get(source_name=source_name)
    except ObjectDoesNotExist:
        return redirect("/miss/%s" % source_name)

    return redirection

def show_miss(request, source_name):
    "Show information about the miss"
    miss = get_missdirection(source_name)
    return render_to_response('index.html',
                              {'miss': miss},
    )

def do_redirect(redirection):
    "Redirect the user"
    if hasattr(redirection, 'get_url'):
        return redirect(redirection.get_url())
    elif isinstance(redirection, str):
        return redirect(redirection)
    else:
        return redirection

def index(request):
    "Grab inbound HTTP_HOST and redirect"
    source_name = request.META['HTTP_HOST']
    if 'localhost' in source_name:
        return welcome(request)
    redirection = get_redirection(source_name=source_name)
    return do_redirect(redirection)

def named_redirect(request, source_name):
    "Redirect from URL"
    redirection = get_redirection(source_name=source_name)
    return do_redirect(redirection)

def welcome(request):
    "Send requets @localhost to /admin"
    return do_redirect("/admin")
